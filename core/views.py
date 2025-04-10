from django.views.generic import ListView, DetailView, CreateView, FormView, View
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from .models import Question, Answer
from .forms import RegisterForm, QuestionForm, AnswerForm


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        try:
            form.save()
            messages.success(self.request, "Registration successful. Please log in.")
        except Exception as e:
            messages.error(self.request, f"Error during registration: {str(e)}")
            return self.form_invalid(form)
        return super().form_valid(form)


class LoginView(AuthLoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy('home')


class HomeView(LoginRequiredMixin, ListView):
    """Home / All Questions"""
    model = Question
    template_name = 'home.html'
    context_object_name = 'questions'
    ordering = ['-created_at']

    def get_queryset(self):
        try:
            return super().get_queryset()
        except Exception as e:
            messages.error(self.request, f"Error loading questions: {str(e)}")
            return []


class AskQuestionView(LoginRequiredMixin, CreateView):
    """Ask Question View"""
    model = Question
    form_class = QuestionForm
    template_name = 'ask_question.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f"Failed to post question: {str(e)}")
            return self.form_invalid(form)


class QuestionDetailView(LoginRequiredMixin, DetailView):
    """Question Detail + Answer Submission"""
    model = Question
    template_name = 'question_detail.html'
    context_object_name = 'question'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Question.DoesNotExist:
            raise Http404("Question not found")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['answers'] = self.object.answers.all().order_by('-created_at')
        except Exception as e:
            context['answers'] = []
            messages.error(self.request, f"Failed to load answers: {str(e)}")
        context['form'] = AnswerForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = AnswerForm(request.POST)
        if form.is_valid():
            try:
                answer = form.save(commit=False)
                answer.user = request.user
                answer.question = self.object
                answer.save()
                messages.success(request, "Answer submitted successfully.")
                return redirect('question_detail', pk=self.object.pk)
            except Exception as e:
                messages.error(request, f"Failed to submit answer: {str(e)}")
        return self.render_to_response(self.get_context_data(form=form))

class LikeAnswerView(LoginRequiredMixin, View):
    """Like Answer View"""
    def post(self, request, answer_id, *args, **kwargs):
        try:
            answer = get_object_or_404(Answer, id=answer_id)

            if answer.user == request.user:
                messages.warning(request, "You cannot like your own answer.")
                return redirect('question_detail', pk=answer.question.id)

            if request.user in answer.likes.all():
                answer.likes.remove(request.user)
                messages.info(request, "You unliked the answer.")
            else:
                answer.likes.add(request.user)
                messages.success(request, "You liked the answer.")

            return HttpResponseRedirect(reverse('question_detail', args=[answer.question.id]))

        except Exception as e:
            messages.error(request, f"Something went wrong: {str(e)}")
            return redirect('home')

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('register/', views.register_view, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     path('ask/', views.ask_question, name='ask_question'),
#     path('question/<int:question_id>/', views.question_detail, name='question_detail'),
#     path('like/<int:answer_id>/', views.like_answer, name='like_answer'),
# ]

from django.urls import path
from .views import (
    RegisterView, LoginView, HomeView,
    AskQuestionView, QuestionDetailView,
    LikeAnswerView
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('ask/', AskQuestionView.as_view(), name='ask_question'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('like/<int:answer_id>/', LikeAnswerView.as_view(), name='like_answer'),
]

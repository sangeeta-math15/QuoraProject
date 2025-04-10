# Quora Clone - Django Web App

## Overview
This is a Django-based web application inspired by Quora. It allows users to:

- Register and log in
- Ask and view questions
- Answer questions
- Like answers (except their own)
- Securely log out

The project focuses on functionality using Django's built-in tools like authentication, forms, and class-based views.

---

## Features

- User registration and login/logout with Django's auth system
- Ask questions (with validation on title/content)
- View all questions and detailed question pages
- Submit answers (with input validation)
- Like others' answers with like toggle functionality
- Restrict liking own answers for fairness
- Secure access to all pages (authentication required)
- Friendly error messages and success notifications

---

## Technologies Used

- Python 3
- Django 4.2
- Postgresql
- Django Forms and ModelForms
- Class-Based Views (CBVs)
---

## Installation and Setup

1. **Clone the repository**
```bash
git clone https://github.com/sangeeta-math15/QuoraProject.git
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Start the development server**
```bash
python manage.py runserver
```

---

##  Authentication Endpoints

### Register
- **URL**: `/register/`
- **Method**: `GET` for form, `POST` to submit
- **Fields**: username, email, password1, password2

### Login
- **URL**: `/login/`
- **Method**: `POST`
- **Redirect**: Homepage on success

### Logout
- **URL**: `/logout/`
- **Method**: `GET`
- **Redirect**: Login page

---

##  Main Features

### Ask a Question
- **URL**: `/ask/`
- **Method**: GET and POST
- **Fields**: Title (min 10 chars), Content (non-empty)

### View Questions
- **URL**: `/`
- Lists all questions in reverse chronological order

### Answer a Question
- **URL**: `/question/<question_id>/`
- Shows question detail and form to post an answer
- Only logged-in users can answer

### Like an Answer
- **URL**: `/like/<answer_id>/`
- Like/unlike an answer
- Cannot like own answer (both backend and template validation)

---

## Validations

- Registration:
  - Unique email check
  - Password match and strength
- Question:
  - Title minimum 10 characters
  - Non-empty content
- Answer:
  - Non-empty or whitespace-only content not allowed
- Likes:
  - User cannot like their own answer

---

##  Testing the App

1. Register a new user and log in.
2. Post a new question via `/ask/`
3. View questions from homepage `/`
4. Click into a question and post an answer.
5. Like someone else's answer. Try to like your own to verify restriction.
6. Try accessing `/ask/` or `/question/<id>/` while logged out to verify redirect.

---


---

## Requirements
```txt
asgiref==3.8.1
Django==4.2.20
psycopg2-binary==2.9.10
python-dotenv==1.0.1
sqlparse==0.5.3
typing_extensions==4.13.1```

---



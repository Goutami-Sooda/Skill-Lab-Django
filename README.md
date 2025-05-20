# Django Skill Lab Workshop

## Project Theme: Task Tracker / To-Do List App

## 🌟 Learning Objectives

By the end of the session, students will:

* Understand what Django is and where it fits in the web development ecosystem.
* Learn MVT architecture and how Django implements it.
* Be able to create a simple Django project with views, models, and templates.
* Understand database integration using SQLite.
* Get introduced to APIs, CORS, and how Django can serve as a backend for frontend frameworks.
* Build and run a mini-project (A To-Do app).

---

## ⏰ Proposed Timeline & Topics

### ☕ 9:30 AM - 11:00 AM

#### **Session 1: Intro to Django & Web Basics (PPT)**

* What is a Web Framework? (Static vs Dynamic Sites)
* Why Django? (Speed, Security, Scalability, Batteries-included)
* Django vs other frameworks (like Flask)
* How Django follows the MVT (Model–View–Template) architecture
* Real-world companies using Django (Instagram, Disqus, etc.)
* **Interactive Element**: Quick poll or quiz on web terms

#### **Session 2: Project Setup & “Hello World!”**

Topics:

* Installing Python, pip, Django
* `django-admin startproject` and folder structure
* Creating a new app using `python manage.py startapp tasks`
* URL routing & views
* Rendering a basic HTML page

**Hands-on Task:**

* Set up the project
* Render a "Hello, Django!" page

> Code for this session is available in the `initial-setup` branch

---

### ☕ 11:30 AM - 1:30 PM

#### **Session 3: Models, Database & Admin Panel**

Topics:

* Creating a Task model (`title`, `description`, `completed`, `created_at`)
* SQLite integration and migrations
* Using Django ORM to query data
* Enabling Django Admin and adding tasks manually

**Hands-on Task:**

* Create and migrate the Task model
* Add sample tasks using Admin Panel

> Code for this session is available in the `models-db-admin` branch


#### **Session 4: Forms, Templates & MVP Concepts**

Topics:

* `forms.ModelForm` to create task submission form
* Displaying tasks using templates
* Django template syntax (loops, conditions, filters)
* What is an MVP and how Django helps you build one fast
* **Discussion**: MVP example - To-Do App with just add + list tasks

**Hands-on Task:**

* Build form to add tasks
* Show task list in UI


> Code for this session is available in the `session4-forms-templates-mvp` branch

---

### ☕ 2:30 PM - 4:30 PM

#### **Session 5: APIs, CORS, & REST Basics**

Topics:

* What is an API? REST basics (GET, POST)
* Install and set up Django REST Framework
* Create serializers and API views for tasks
* Enable CORS using `django-cors-headers`
* Demonstrate API testing with browser or `fetch()`

**Hands-on Task:**

* Create `/api/tasks/` endpoint to view all tasks
* Show POST request to add a task, and GET to fetch tasks and display

> Code for this session is available in the `api-cors-rest` branch


#### **Session 6: Mini Project Build + Wrap Up**

Mini Project: Choose from the following or create your own idea

**Project Ideas:**

* Bookstore App
* Event Registration App
* Library Management System
* Job Application Portal (Like Unstop)
* Feedback Collector with Analytics

**Key Components:**

* **Model:** Task (`title`, `desc`, `status`, `created_at`)
* **Form:** Add new task
* **Template:** Display task list with status
* **API:** View tasks as JSON, add task
* **CORS:** Enable frontend access (optional bonus)

**Stretch Goals:**

* Add update/delete actions
* Add filtering (e.g., show completed tasks only)
* Deploy project using PythonAnywhere or Render

---

## 📁 Repository Structure

* **main**: Workshop overview, session plans and completed project codebase
* **initial-setup**: Code and instructions for setting up Django project and rendering a basic view (Session 2)
* **models-db-admin**: Code for Task model, migrations, and admin integration (Session 3)
* **session4-forms-templates-mvp**: Forms, template views, and task list UI (Session 4)
* **api-cors-rest**: DRF setup, API endpoints, and CORS (Session 5)

---

Happy Learning & Building! 🤝🏼🌟

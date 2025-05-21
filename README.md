# Skill-Lab-Django
# Session 4: Build the Core Features of the Django To-Do App

This session focuses on building the core functionalities of a basic To-Do application using Django:
- Create and manage tasks
- Display task list
- Add new tasks via form
- Mark tasks as completed

---

## Step 1: Create a Model Form for Task Input

  File: `tasks/forms.py`

- Create a `TaskForm` class that uses `Task` model and allows input of `title` and `description`.

---

## Step 2: Add Views for Listing and Updating Tasks

  File: `tasks/views.py`

- Modify or add the following views:
  - `home` – for a simple welcome message. This is already there
  - `task_list` – to show all tasks and handle new task submissions.
  - `mark_completed` – to mark a specific task as completed.

---

## Step 3: Set Up Templates for UI

 Folder: `tasks/templates/tasks/`  
 File: `task_list.html`

- Create an HTML file for displaying the task list and form.
- Use Django Template Language to dynamically loop through tasks and show status.

---

##  Step 4: Configure App-Level URLs

 File: `tasks/urls.py`

- Add path for:
  - `''` → task list
  - `'complete/<int:pk>/'` → mark a task as completed

---

##  Step 5: Include App URLs in Project URL Config

  File: `todo_project/urls.py`

- Use `include()` to mount the `tasks.urls` into the main project routing.

---


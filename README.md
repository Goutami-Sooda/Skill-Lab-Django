# Django Task Management Application

A complete task management system built with Django featuring CRUD operations and admin interface.

## Model Definition <a name="model-definition"></a>

### 1.Task Model
Location: `tasks/models.py`

```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```
Explanation:

title: Short text field (task name)

description: Longer optional text field

completed: Boolean field (True/False)

created_at: Automatically sets timestamp when task is created

__str__: Displays title instead of "Task object" in admin

### 2.Make Migrations
This step prepares the model to be added to the database.

```bash
python manage.py makemigrations

Expected Output:
```Migrations for 'tasks':
  tasks/migrations/0001_initial.py
```
### 3.Apply Migrations
Creates the database table for the model.

```bash
python manage.py migrate
```
Expected Output includes:
`Applying tasks.0001_initial... OK`

### 4.Register the Model in Admin Panel
Location: `tasks/admin.py`

```python
from django.contrib import admin
from .models import Task

admin.site.register(Task)
```
This will display the Task model in the Django admin dashboard.

### 5.Create Superuser to Access Admin
Run this command and follow the prompts:

```bash
python manage.py createsuperuser
```
You'll be prompted to enter:

*Username:
*Email (optional):
*Password:

### 6.Run the Development Server

```bash
python manage.py runserver
```

Now visit the admin panel at:
🌐 http://127.0.0.1:8000/admin

## Features
*Create, read, update, and delete tasks
*Mark tasks as completed
*Automatic timestamping of created tasks
*Admin interface for easy management

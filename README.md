# Django Task Management Application

A complete task management system built with Django featuring CRUD operations and admin interface.

## Table of Contents
- [Model Definition](#model-definition)
- [Database Setup](#database-setup)
- [Admin Configuration](#admin-configuration)
- [Running the Application](#running-the-application)
- [Features](#features)
- [Requirements](#requirements)

## Model Definition <a name="model-definition"></a>

### Task Model
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

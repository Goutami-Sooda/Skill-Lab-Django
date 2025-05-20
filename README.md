# Session 5: APIs, CORS, & REST Basics

This session introduces you to APIs, HTTP methods, REST architecture, and how to implement them in your Django project using **Django REST Framework (DRF)**. By the end, your To-Do app will support task management via API and frontend integration using `fetch()`.


## 🌐 What is an API?

An **API (Application Programming Interface)** allows two systems — like your Django backend and a frontend app — to communicate. In web development, APIs are typically used to send and receive data in **JSON** format via HTTP.

🔁 **Think of it like a restaurant:**
- You (the client) look at the menu (API docs).
- You place your order via the waiter (API request).
- The kitchen (backend) prepares your food (data).
- The waiter brings it back to you (API response).


## 🚦 HTTP Methods Used in APIs

| Method | Purpose           | Example (To-Do App)    |
|--------|-------------------|------------------------|
| GET    | Read data         | Fetch task list        |
| POST   | Create data       | Add a new task         |
| PUT    | Update data       | Edit task details      |
| PATCH  | Partial update    | Mark task as completed |
| DELETE | Remove data       | Delete a task          |


## 🔄 What is REST?

REST (Representational State Transfer) is an architecture style for designing networked APIs. A RESTful API:

- Uses **HTTP methods** meaningfully (GET, POST, PUT, DELETE).
- Treats everything as a **resource** (e.g., `/api/tasks/`).
- Is **stateless** — every request is independent.
- Communicates using **JSON** for ease of use.


## 🎯 Why Use APIs?

- Decouple your frontend from the backend.
- Test endpoints with tools like **Postman**.
- Enable integration with mobile apps or third-party systems.
- Build more powerful and flexible applications.

---

## 🛠️ Implementation Steps

### ✅ Step 1: Install Required Packages

Make sure to install Django REST Framework and CORS headers.

```bash
pip install djangorestframework
pip install django-cors-headers
```


### ✅ Step 2: Configure Django Settings

In `settings.py`:
- Add `'rest_framework'`, `'corsheaders'`, and your app (`'tasks'`) to `INSTALLED_APPS`.
- Add `'corsheaders.middleware.CorsMiddleware'` to the `MIDDLEWARE` list.
- For development/testing, set:
  ```python
  CORS_ALLOW_ALL_ORIGINS = True
  ```
📁 File to check: settings.py


### ✅ Step 3: Create Serializer

Define a serializer to convert between Django models and JSON.

📁 **File**: `tasks/serializers.py`  
🔧 **Class**: `TaskSerializer`



### ✅ Step 4: Create API Views

Use function-based views to handle `GET` and `POST` requests for tasks.

📁 **File**: `tasks/views.py`  
🔧 **Function**: `task_api(request)`



### ✅ Step 5: Wire API Routes

Add URL patterns to expose the API endpoint.

📁 **File**: `tasks/urls.py`  
🔗 **Path**: 
```python
path('api/tasks/', views.task_api, name='task-api')
```

### ✅ Step 6: Test API Endpoints

Use a browser or Postman to:

* **GET all tasks**:
  [http://127.0.0.1:8000/api/tasks/](http://127.0.0.1:8000/api/tasks/)

* **POST a new task** with JSON body:

```json
{
  "title": "Test API Task",
  "description": "Added via API"
}
```


### ✅ Step 7: Use `fetch()` in Frontend

Use JavaScript’s `fetch()` method to:

* Fetch tasks via **GET**
* Add new tasks via **POST**
* Mark tasks as completed using **PATCH**

📁 **File**: `templates/task_list.html` *(or `task.html`)*



### 🔧 Additional Integrations

* Create a view named `tasks_home` to render the template.
  📁 **File**: `tasks/views.py`

* Update URLs to include this view.
  📁 **File**: `tasks/urls.py`

* Add a PATCH-based API endpoint to mark tasks as complete.
  📁 **Files**: `tasks/views.py`, `tasks/urls.py`

* Update your HTML to dynamically render tasks and include a **"Mark Complete"** button using JavaScript and `fetch()`.

---

### 🔍 Explore the Code

This session's code is available in the **`api-cors-rest`** branch. Use it to:

* Learn how to build API endpoints using **Django REST Framework**.
* Understand how to integrate APIs with a frontend using **JavaScript**.
* Extend your project with more features like **DELETE**, **PUT**, and **authentication**.

---

📘 **Happy coding!**
Let your backend serve data like a pro 🚀


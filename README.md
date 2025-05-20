# Session 2: Project Setup & "Hello World!"

Official Django Documentation: [https://docs.djangoproject.com/en/5.2/contents/](https://docs.djangoproject.com/en/5.2/contents/)


## 🎯 Goal

Create a working Django project named `todo_app` with a simple home page rendered through a view.


## 🧰 Step-by-Step Instructions

### ✅ Step 1: Install Python and pip (if not installed)

* Check if Python and pip are installed:

  * `python --version`
  * `pip --version`
* If not installed, download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/)

  * ✅ Make sure to check "Add Python to PATH" during installation

### ✅ Step 2: Install Django

* Use pip to install Django (globally or in a virtual environment)
  ```python
  pip install django
  ```
* Verify installation

### ✅ Step 3: Create Django Project

* Create a project named `todo_app`
* Navigate into the project folder
* Project folder structure to reference:

  * `todo_app/`

    * `manage.py`
    * `todo_app/`

      * `__init__.py`, `settings.py`, `urls.py`, `asgi.py`, `wsgi.py`

### ✅ Step 4: Run Development Server

* Start the development server
* Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to confirm successful setup

### ✅ Step 5: Create an App Named `tasks`

* Add a new app to the project
* New folder structure under `todo_app/` should include:

  * `tasks/`

    * `views.py`, `models.py`, `admin.py`, `apps.py`, `tests.py`, `migrations/`, `__init__.py`

### ✅ Step 6: Register the App

* Open `todo_app/settings.py`
* Add `'tasks',` to the `INSTALLED_APPS` list

### ✅ Step 7: Create a Basic View

* Open `tasks/views.py`
* Define a `home` view that returns a simple HTTP response

### ✅ Step 8: Wire Up URLs

#### A. Create `urls.py` in `tasks/`

* Map the root path to the `home` view in `tasks/urls.py`

#### B. Include tasks.urls in Project URLs

* Open `todo_app/urls.py`
* Use `include()` to add `tasks.urls` to the main URL patterns

### ✅ Step 9: Run the Server and Test

* Start the development server again
* Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* You should see the message: **"Hello, Django! Welcome to your To-Do App."**

This confirms your Django app and routing are working! 🎉

---

## 🧩 Optional Add-on: Render an HTML Template

### Step 1: Create a Templates Folder

* Inside `tasks/`, create a `templates/` folder
* Add an HTML file named `home.html` inside `templates/`

### Step 2: Update the View

* Modify `tasks/views.py` to use the `render()` method to serve `home.html`

---

✅ Done! You've laid the groundwork for building out the Task Tracker App. Move to the next branch `models-db-admin` to continue development!

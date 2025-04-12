# TweetApp

TweetApp is a Django-based web application that allows users to post and view tweets. It demonstrates the use of Django's core functionalities, including models, views, templates, and static files.

## Features

- User authentication (login/logout)
- Create, read, update, and delete tweets
- Responsive user interface with Bootstrap
- Media uploads for user profiles and tweets

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/WaqasAly/TweetApp.git](https://github.com/WaqasAly/TweetApp.git)
    cd TweetApp
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a superuser (optional):**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7.  **Visit** `http://127.0.0.1:8000/` in your browser.

## Project Structure
Markdown

# TweetApp

TweetApp is a Django-based web application that allows users to post and view tweets. It demonstrates the use of Django's core functionalities, including models, views, templates, and static files.

## Features

- User authentication (login/logout)
- Create, read, update, and delete tweets
- Responsive user interface with Bootstrap
- Media uploads for user profiles and tweets

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/WaqasAly/TweetApp.git](https://github.com/WaqasAly/TweetApp.git)
    cd TweetApp
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a superuser (optional):**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7.  **Visit** `http://127.0.0.1:8000/` in your browser.

## Project Structure

TweetApp/
├── chaicenter/             # Main Django app
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── TweetApp/               # Project settings
│   ├── init.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/                  # Uploaded media files
├── static/                 # Static files
├── templates/              # Global templates
├── manage.py
└── requirements.txt

## Configuration

In `settings.py`, ensure the following configurations are set for static and media files:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  ```
In the project's urls.py, add the following to serve media files during development:

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chaicenter.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

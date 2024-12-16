# Django Project Management API

## Context
- [Project Setup](#project-setup)
- [API Documentation](#api-documentation)
    - [Users](#users)
    - [Projects](#projects)
    - [Tasks](#tasks)
    - [Comments](#comments)
- [Create Documentation Using Swagger](#create-documentation-using-swagger)

## Implementation
### Project Setup
1. At first Create Environment:
    ```cmd
    python-m venv env
    ```
2. After Create envirionment activate the environment:
    ```cmd
    .\env\Scripts\activate
    ```
3. Install Dependencies:
    ```cmd
    pip install -r requirements.txt
    ```
4. Create a Djnago Project:
    ```cmd
    django-admin startproject project_management
    ```
5. Change current directory to `project_management` folder:
    ```cmd
    cd project_management
    ```
6. Create a Django App:
    ```cmd
    django-admin startapp api_app
    ```
7. Update `settings.py` to Add `rest_framework` and `app_name` to `INSTALLED_APPS`:
    ```python
    INSTALLED_APPS = [
    ......
    ......
    'rest_framework',
    'api_app',
    ]
    ```

⬆️ [Go to Context](#context)
### Folder Stracture
```cmd
Main-Folder/
│
└── project_management/
    │
    ├── project_management/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │
    ├── api_app/
    │   ├── migrations/
    │   ├── models.py
    │   ├── serializers.py
    │   ├── views.py
    │   └── urls.py
    │
    ├── requirements.txt
    ├── .gitignore
    └── manage.py
```

### Final Setup
- After Implement the Model Migrate the database:
    ```cmd
    py manage.py makemigrations
    py manage.py migrate
    ```
- Create superuser
    ```cmd
    py manage.py createsuperuser
    ```
⬆️ [Go to Context](#context)

# API Documentation
To View Swagger Documentation:
```cmd
URL: `/api/docs/`
```
To View Redoc API Documentation:
```cmd
URL: `/api/redoc/`
```
## Users
### 1. User Register:
- Register a new user.
- URL: `/users/register/`
- Method: `POST`
- **Request Body:**
    ```json
    {
    "username": "string",
    "email": "user@example.com",
    "password": "string",
    "first_name": "string",
    "last_name": "string"
    }
    ```
- **Response Example:**
    ```json
    {
        "user": {
            "id": 1,
            "username": "username",
            "email": "user@example.com",
            "password": "userpassword",
            "first_name": "user_firstname",
            "last_name": "user_lastname",
        },
        "message": "User registered successfully",
        "refresh": "jwt_refresh_token",
        "access": "jwt_access_token"
    }
    ```
### 2. User Login:
- Authenticates an existing user.
- URL: `/users/login/`
- Method: `POST`
- **Request Body:**
    ```json
    {
    "username": "string",
    "password": "string"
    }
    ```
- **Response Example:**
    ```json
    {
       "user": {
        "id": 1,
        "username": "username",
        "password": "userpassword"
        },
        "refresh": "jwt_refresh_token",
        "access": "jwt_access_token"
    }
    ```
### 3. Update User:
- Updates the details of an existing user.
- URL: `/users/{user_id}/`
- Method: `PUT` or `PATCH`

### 4. Delete User:
- Deletes an existing user.
- URL: `/users/{user_id}/`
- Method: `DELETE`

⬆️ [Go to Context](#context)
## Projects 
### 5. List Projects:
- Retrieves all projects.
- URL: `/projects/`
- Method: `GET`
- **Response Body:**
    ```json
    [
        {
            "id": 1,
            "Name": "Project A",
            "Description": "Description of Project A",
            "Created_at": "2024-12-16T10:51:39.178967Z",
            "Owner": 1
        },
        {
            "id": 2,
            "Name": "Project B",
            "Description": "Description of Project  B",
            "Created_at": "2024-12-16T10:55:26.737989Z",
            "Owner": 2
        }
    ]
    ```
### 6. Create Project:
- Creates a new project.
- URL: `/users/`
- Method: `POST`
- **Request Body:**
    ```json
    {
        "Name": "Project A",
        "Description": "Description of Project  A",
        "Owner": 2
    }
    ```
- **Response Body:**
    ```json
    {
        "id": 1,
        "Name": "Project A",
        "Description": "Description of Project A",
        "Created_at": "2024-12-16T10:51:39.178967Z",
        "Owner": 1
    }
    ```

### 7. Update Project:
- Updates the details of an existing project.
- URL: `/projects/{project_id}/`
- Method: `PUT` or `PATCH`

### 8. Delete Project:
- Deletes an existing project.
- URL: `/projects/{project_id}/`
- Method: `DELETE`

⬆️ [Go to Context](#context)
## Tasks
### 9. List Tasks for a Project:
- Retrieves tasks associated with a specific project.
- URL: `/projects/{project_id}/tasks/`
- Method: `GET`
- **Response Body:**
    ```json
    [
        {
            "id": 1,
            "Title": "Task 1",
            "Description": "Description of Task 1",
            "Status": "To Do",
            "Priority": "Medium",
            "Created_at": "2024-12-16T00:29:37.508463Z",
            "Due_date": "2024-12-19T17:04:00Z",
            "Assigned_to": 2,
            "Project": 2
        },
        {
            "id": 3,
            "Title": "Task 3",
            "Description": "Description of Task 3",
            "Status": "To Do",
            "Priority": "Medium",
            "Created_at": "2024-12-16T11:01:26.577795Z",
            "Due_date": "2024-12-18T00:36:51.201069Z",
            "Assigned_to": 3,
            "Project": 2
        }
    ]
    ```

### 10. Create Task for a Project:
- Creates a new task under a specific project.
- URL: `/projects/{project_id}/tasks/`
- Method: `POST`
- **Request Body:**
    ```json
    {
        "Title": "Task 3",
        "Description": "Description of Task 3",
        "Status": "To Do",
        "Priority": "Medium",
        "Due_date": "2024-12-20T10:00:00Z",
        "Assigned_to": 3,
        "Project": 2
    }
    ```
- **Response Body:**
    ```json
    {
        "id": 3,
        "Title": "Task 3",
        "Description": "Description of Task 3",
        "Status": "To Do",
        "Priority": "Medium",
        "Created_at": "2024-12-16T11:01:26.577795Z",
        "Due_date": "2024-12-20T10:00:00Z",
        "Assigned_to": 3,
        "Project": 2
    }
    ```
### 11. Update Task:
- Updates the details of an existing task.
- URL: `/tasks/{task_id}/`
- Method: `PUT` or `PATCH`

### 12. Delete Task:
- Deletes an existing task.
- URL: `/tasks/{task_id}/`
- Method: `DELETE`

⬆️ [Go to Context](#context)
## Comments
### 13. List Comments for a Task:
- Retrieves comments associated with a specific task.
- URL: `/tasks/{task_id}/comments/`
- Method: `GET`
- **Response Body:**
    ```json
    [
        {
            "id": 1,
            "Content": "Comment 1",
            "Created_at": "2024-12-16T00:37:02.366935Z",
            "User": 2,
            "Task": 1
        },
        {
            "id": 2,
            "Content": "Comment 2",
            "Created_at": "2024-12-16T00:37:35.404217Z",
            "User": 2,
            "Task": 2
        }
    ]
    ```

### 14. Create Comment for a Task:
- Creates a new comment under a specific task.
- URL: `/tasks/{task_id}/comments/`
- Method: `POST`
- **Request Body:**
    ```json
    {
        "Content": "Comment 2",
        "User": 2,
    }
    ```
- **Response Body:**
    ```json
    {
        "id": 2,
        "Content": "Comment 2",
        "Created_at": "2024-12-16T00:37:35.404217Z",
        "User": 2,
        "Task": 2
    }
    ```
### 15. Update Comment:
- Updates the content of an existing comment.
- URL: `/comments/{comment_id}/`
- Method: `PUT` or `PATCH`

### 16. Delete Comment:
- Deletes an existing comment.
- URL: `/comments/{comment_id}/`
- Method: `DELETE`

⬆️ [Go to Context](#context)

## Create Documentation Using Swagger
Using Swagger in Django can simplify the process of documenting APIs and provide an intuitive interface to test them.

### 1. Install Required Libraries
```cmd
pip install drf-yasg
```

### 2. Configure Swagger in Django
```cmd
INSTALLED_APPS = [
    ...
    'drf_yasg',
]
```

### 3. Configure Swagger URLS: In `urls.py`
```python
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Project Management API",
        default_version="v1",
        description="API documentation for the Project Management Tool",
    ),
    public=True,
    permission_classes=(AllowAny),
)

urlpatterns = [
    ....
    ....
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]
```

⬆️ [Go to Context](#context)
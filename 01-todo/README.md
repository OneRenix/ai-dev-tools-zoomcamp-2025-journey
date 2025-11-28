# TODO Django App

This is a simple yet extensible TODO Django application created for the Zoomcamp project. It provides core functionality for managing personal tasks with due dates, priorities, tags, subtasks, and comments.

## Table of Contents

- [Features](#features)
- [Quickstart](#quickstart)
- [Project Structure](#project-structure)
- [Models](#models)
- [Views and URLs](#views-and-urls)
- [Templates](#templates)
- [Contributing](#contributing)
- [Future Enhancements](#future-enhancements)

## Features

- **CRUD Operations**: Create, Read, Update, and Delete TODOs.
- **Due Dates**: Assign specific deadlines to tasks.
- **Task Resolution**: Mark TODOs as resolved or unresolved.
- **Prioritization**: Assign priority levels (Low, Medium, High) to tasks.
- **Tagging**: Categorize TODOs with multiple tags for better organization.
- **Subtasks**: Break down complex TODOs into smaller, manageable subtasks.
- **Comments**: Add comments to TODOs for additional context or notes.
- **Admin Interface**: Manage all models (TODOs, Tags, Subtasks, Comments) through Django's built-in admin.

## Quickstart

Follow these steps to get the TODO application up and running locally.

1.  **Navigate to the project directory**:
    ```bash
    cd 01-todo
    ```

2.  **Create a virtual environment and install dependencies**:
    A virtual environment (`.venv`) is already included in this workspace. If for some reason it's not present or you wish to recreate it, you can do so:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Apply database migrations**:
    This sets up the necessary database tables for your models.
    ```bash
    ./.venv/bin/python manage.py migrate
    ```

4.  **Create a superuser (optional but recommended)**:
    This allows you to access the Django admin interface to manage your TODOs, tags, subtasks, and comments.
    ```bash
    ./.venv/bin/python manage.py createsuperuser
    ```
    Follow the prompts to create your admin account.

5.  **Run the development server**:
    ```bash
    ./.venv/bin/python manage.py runserver 0.0.0.0:8000
    ```

6.  **Access the application**:
    -   Open your web browser and navigate to `http://127.0.0.1:8000/` to view the TODO app.
    -   Access the admin interface at `http://127.0.0.1:8000/admin/` to manage models.

## Project Structure

The project follows a standard Django structure:

```
01-todo/
├── .venv/                      # Python Virtual Environment
├── db.sqlite3                  # SQLite database file
├── manage.py                   # Django's command-line utility
├── README.md                   # This documentation file
├── requirements.txt            # Python dependencies
├── tasks/                      # Django app for TODOs
│   ├── migrations/             # Database migrations for the `tasks` app
│   ├── templates/              # HTML templates specific to the `tasks` app
│   │   └── tasks/
│   │       ├── todo_confirm_delete.html
│   │       ├── todo_form.html
│   │       └── todo_list.html
│   ├── __init__.py
│   ├── admin.py                # Admin site configuration for `tasks` models
│   ├── apps.py                 # App configuration
│   ├── forms.py                # Django forms for `Todo` model
│   ├── models.py               # Database models for `Todo`, `Tag`, `Subtask`, `Comment`
│   ├── tests.py                # (Future) Unit tests for the `tasks` app
│   └── views.py                # Logic for handling requests and returning responses
├── templates/                  # Project-level templates (e.g., base layout)
│   └── base.html
└── todo_project/               # Main Django project configuration
    ├── __init__.py
    ├── asgi.py                 # ASGI configuration for async apps
    ├── settings.py             # Project settings
    ├── urls.py                 # Project-level URL declarations
    └── wsgi.py                 # WSGI configuration for traditional apps
```

## Models

The `tasks/models.py` file defines the database schema for the TODO application.

-   **`Todo`**: The central model for tasks.
    -   `title` (CharField): The name of the TODO.
    -   `description` (TextField): Detailed description of the TODO (optional).
    -   `owner` (ForeignKey to `User`): The user who owns the TODO (optional).
    -   `due_date` (DateField): The target completion date (optional).
    -   `resolved` (BooleanField): Indicates if the TODO is completed.
    -   `priority` (CharField, choices: `Low`, `Medium`, `High`): The urgency of the task.
    -   `tags` (ManyToManyField to `Tag`): Categories for the TODO (optional).
    -   `created_at` (DateTimeField): Timestamp when the TODO was created.
    -   `updated_at` (DateTimeField): Timestamp of the last update.

-   **`Tag`**: A simple model for categorizing TODOs.
    -   `name` (CharField): The tag's name (unique).

-   **`Subtask`**: Represents a smaller, dependent task within a main `Todo`.
    -   `todo` (ForeignKey to `Todo`): The parent TODO.
    -   `title` (CharField): The name of the subtask.
    -   `completed` (BooleanField): Indicates if the subtask is done.
    -   `created_at` (DateTimeField): Timestamp when the subtask was created.

-   **`Comment`**: For adding notes or discussions to a `Todo`.
    -   `todo` (ForeignKey to `Todo`): The parent TODO.
    -   `text` (TextField): The content of the comment.
    -   `created_by` (ForeignKey to `User`): The user who made the comment (optional).
    -   `created_at` (DateTimeField): Timestamp when the comment was created.

## Views and URLs

The `tasks/views.py` file contains the logic for handling web requests and interacting with the models, while `tasks/urls.py` defines the URL patterns for accessing these views. The main project `todo_project/urls.py` includes the `tasks` app's URLs.

-   **`TodoListView`**: Displays a list of all TODOs.
    -   URL: `/`
-   **`TodoCreateView`**: Handles the creation of new TODOs.
    -   URL: `/todo/create/`
-   **`TodoUpdateView`**: Manages editing existing TODOs.
    -   URL: `/todo/<int:pk>/edit/`
-   **`TodoDeleteView`**: Confirms and handles the deletion of a TODO.
    -   URL: `/todo/<int:pk>/delete/`
-   **`toggle_resolved`**: A functional view to quickly switch a TODO's resolved status.
    -   URL: `/todo/<int:pk>/toggle_resolved/`

## Templates

The application uses Django's template system to render HTML.

-   `templates/base.html`: The base HTML structure and includes Bootstrap for styling.
-   `tasks/templates/tasks/todo_list.html`: Displays the list of TODOs, showing title, due date, priority, tags, resolved status, and subtask count. Provides links for editing, deleting, and toggling resolution.
-   `tasks/templates/tasks/todo_form.html`: A reusable form for creating and editing TODOs, including fields for title, description, due date, priority, resolved status, and tags.
-   `tasks/templates/tasks/todo_confirm_delete.html`: A confirmation page before deleting a TODO.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix (`git checkout -b feature/your-feature-name`).
3.  Make your changes and write tests if applicable.
4.  Ensure all tests pass (`./.venv/bin/python manage.py test`).
5.  Commit your changes (`git commit -m 'feat: Add new feature'`).
6.  Push to your fork (`git push origin feature/your-feature-name`).
7.  Open a Pull Request to the `main` branch of the original repository.

## Future Enhancements

Here are some ideas for extending the TODO app:

-   **User Authentication and Authorization**: Implement proper user accounts, allowing users to only see and manage their own TODOs.
-   **Advanced Filtering and Sorting**: Add options to filter TODOs by owner, tags, priority, due date range, and implement dynamic sorting.
-   **Pagination**: Implement pagination for the TODO list to handle a large number of tasks efficiently.
-   **Search Functionality**: Add a search bar to find TODOs by title or description.
-   **API Endpoints**: Create a RESTful API for TODOs to allow integration with other services or frontends (e.g., using Django REST Framework).
-   **Notifications**: Implement email or in-app notifications for upcoming due dates or assigned tasks.
-   **Improved UI/UX**: Enhance the user interface with more interactive elements, such as drag-and-drop for reordering tasks, or a calendar view.
-   **Unit and Integration Tests**: Write comprehensive tests for models, forms, views, and URL configurations to ensure robustness and prevent regressions.
-   **CI/CD Pipeline**: Set up continuous integration and deployment for automated testing and deployment.

from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.TodoListView.as_view(), name="todo_list"),
    path("todo/create/", views.TodoCreateView.as_view(), name="todo_create"),
    path("todo/<int:pk>/edit/", views.TodoUpdateView.as_view(), name="todo_edit"),
    path("todo/<int:pk>/delete/", views.TodoDeleteView.as_view(), name="todo_delete"),
    path("todo/<int:pk>/toggle_resolved/", views.toggle_resolved, name="todo_toggle_resolved"),
]

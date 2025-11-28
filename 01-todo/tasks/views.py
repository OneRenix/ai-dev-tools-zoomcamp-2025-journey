from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Todo
from .forms import TodoForm


class TodoListView(ListView):
	model = Todo
	template_name = "tasks/todo_list.html"
	context_object_name = "todos"


class TodoCreateView(CreateView):
	model = Todo
	form_class = TodoForm
	template_name = "tasks/todo_form.html"
	success_url = reverse_lazy("tasks:todo_list")


class TodoUpdateView(UpdateView):
	model = Todo
	form_class = TodoForm
	template_name = "tasks/todo_form.html"
	success_url = reverse_lazy("tasks:todo_list")


class TodoDeleteView(DeleteView):
	model = Todo
	template_name = "tasks/todo_confirm_delete.html"
	success_url = reverse_lazy("tasks:todo_list")


def toggle_resolved(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	todo.resolved = not todo.resolved
	todo.save()
	return redirect("tasks:todo_list")

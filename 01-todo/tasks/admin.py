
from django.contrib import admin
from .models import Todo, Tag, Subtask, Comment


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "due_date", "resolved", "created_at")
	list_filter = ("resolved", "due_date")
	search_fields = ("title", "description")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ("name",)
	search_fields = ("name",)


@admin.register(Subtask)
class SubtaskAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "todo", "completed", "created_at")
	list_filter = ("completed",)
	search_fields = ("title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ("id", "todo", "created_by", "created_at")
	search_fields = ("text",)

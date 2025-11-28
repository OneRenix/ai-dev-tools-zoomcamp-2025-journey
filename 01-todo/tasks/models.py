from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Todo(models.Model):
	class Priority(models.TextChoices):
		LOW = "low", "Low"
		MEDIUM = "medium", "Medium"
		HIGH = "high", "High"

	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	owner = models.ForeignKey(
		User,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name="todos",
	)
	due_date = models.DateField(null=True, blank=True)
	resolved = models.BooleanField(default=False)
	priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.MEDIUM)
	tags = models.ManyToManyField("Tag", blank=True, related_name="todos")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self) -> str:  # pragma: no cover - repr only
		return f"{self.title} ({'resolved' if self.resolved else 'open'})"


class Tag(models.Model):
	name = models.CharField(max_length=50, unique=True)

	class Meta:
		ordering = ["name"]

	def __str__(self) -> str:  # pragma: no cover - repr only
		return self.name


class Subtask(models.Model):
	todo = models.ForeignKey(Todo, related_name="subtasks", on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self) -> str:  # pragma: no cover - repr only
		return f"{self.title} ({'done' if self.completed else 'todo'})"


class Comment(models.Model):
	todo = models.ForeignKey(Todo, related_name="comments", on_delete=models.CASCADE)
	text = models.TextField()
	created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self) -> str:  # pragma: no cover - repr only
		return f"Comment on {self.todo.title} by {self.created_by or 'anonymous'}"

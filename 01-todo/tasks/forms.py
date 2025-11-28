from django import forms
from .models import Todo, Tag


class TodoForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), required=False)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), required=False, widget=forms.SelectMultiple(attrs={"size": 5})
    )

    class Meta:
        model = Todo
        fields = ["title", "description", "due_date", "resolved", "priority", "tags"]

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Category, Task


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.user = user

    class Meta:
        model = Category
        fields = ["name"]

    def clean_name(self):
        if (
            Category.objects.filter(name=self.cleaned_data["name"], owner=self.user)
            .exclude(pk=self.instance.pk)
            .exists()
        ):
            raise forms.ValidationError("Category is already created!")
        return self.cleaned_data["name"]


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields["category"].queryset = Category.objects.filter(owner=self.user)
        self.fields["category"].empty_label = "Choose your category"

    class Meta:
        model = Task
        fields = ["title", "description", "status", "category"]


class StyledUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control mb-2"

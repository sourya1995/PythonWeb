from django import forms
from .models import Post

class SearchForm(forms.Form):
    q = forms.CharField()

class TestForm(forms.Form):
    text = forms.CharField()
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=10)
    email = forms.EmailField()

    def clean_integer(self):
        integer = self.cleaned_data.get("integer")
        if integer <= 10:
            raise forms.ValidationError("The integer must be greater than 10")
        return integer


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
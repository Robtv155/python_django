from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from contenido.models import Post, Comment

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electronico")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo electronico")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

class PostForm(forms.ModelForm):
    tag_string = forms.CharField(required= False, label="Tags", help_text="Separar tags con comas")

    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': 'Título',
            'content': 'Contenido',
                    }


class CommentForm(forms.ModelForm):
    tag_string = forms.TextInput

    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Contenido',
                    }

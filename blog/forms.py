from django import forms

from .models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('baslik', 'yazi',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('yazar', 'yazi',)
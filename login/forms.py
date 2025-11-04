# forms.py
from django import forms
from .models import Comment
from .models import Article
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content','image']
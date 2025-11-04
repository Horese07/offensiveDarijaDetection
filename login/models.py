from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)  # Champ image

    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)  # Champ pour le nom de l'auteur
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approuvé = models.BooleanField(default=True)  # Champ pour indiquer si le commentaire est approuvé


    def __str__(self):
        return self.author



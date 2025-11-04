from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('auth/', views.custom_login, name='auth'),
    path('', views.home,name= 'home'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('add_article/', views.add_article, name='add_article'),
    path('article_summary/', views.article_summary, name='article_summary'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('prediction/', views.prediction, name='prediction'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Servir les fichiers médias en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
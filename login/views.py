from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Article
from django.shortcuts import render, redirect
from .forms import ArticleForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Article, Comment
from .forms import CommentForm
from django.contrib.auth.models import User
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from utils.toxic_filter import query, evaluate_response  # Importer la fonction de filtre de toxicité




from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt  # only for testing — remove in production
def prediction(request):
    """
    Vue pour vérifier si un texte est toxique ou non.
    """
    if request.method == 'POST':
        text = request.POST.get('text', '')
        if not text:
            return JsonResponse({'error': 'No text provided'}, status=400)

        # Utiliser la fonction is_toxic existante
        toxic = is_toxic(text)

        return JsonResponse({
            'text': text,
            'is_toxic': toxic,
            'message': 'Toxic comment detected' if toxic else 'Text is clean'
        })
    
    return JsonResponse({'error': 'Only POST method allowed'}, status=405)


def custom_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Charger directement la page "ajouter_article.html"
            return redirect('add_article')
        else:
            return render(request, 'auth.html', {'error': 'Identifiants incorrects'})
    return render(request, 'auth.html')



def home(request):
    articles = Article.objects.all()  # Récupère tous les articles depuis la base de données
    return render(request, 'index.html', {'articles': articles})  # Passe les articles à la page index.html


  # Importer les fonctions du fichier toxic_filter.py

def is_toxic(comment_content):
    """
    Vérifie si un commentaire est toxique en utilisant l'API HuggingFace.
    Retourne True si le commentaire est toxique, False sinon.
    """
    # Préparer la requête pour l'API
    payload = {"inputs": comment_content}
    response = query(payload)

    # Évaluer la réponse pour déterminer si le commentaire est toxique
    result = evaluate_response(response)
    return result == 1  # Retourne True si le commentaire est toxique

def article_detail(request, id):
    """
    Vue pour afficher les détails d'un article et gérer l'ajout de commentaires.
    """
    # Récupérer l'article et ses commentaires approuvés
    article = get_object_or_404(Article, id=id)
    comments = article.comments.filter(approuvé=True)  # Filtrer les commentaires approuvés uniquement

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article  # Associer le commentaire à l'article
            
            # Vérifier si le commentaire est toxique
            if is_toxic(comment.content):
                message = "Votre commentaire est considéré comme toxique et ne sera pas publié."
            else:
                comment.approuvé = True  # Marquer le commentaire comme approuvé
                comment.save()
                message = "Votre commentaire a été ajouté avec succès."
            
            # Recharger la page avec le message et le formulaire vide
            return render(request, 'article_detail.html', {
                'article': article,
                'comments': comments,
                'form': CommentForm(),  # Nouveau formulaire vide
                'message': message
            })
    else:
        form = CommentForm()

    return render(request, 'article_detail.html', {
        'article': article,
        'comments': comments,
        'form': form
    })





def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()  # Sauvegarder l'article dans la base de données
            #return redirect('home')  # Redirige vers la page d'accueil (ou vers une autre page)
    else:
        form = ArticleForm()  # Affiche un formulaire vide

    return render(request, 'add_article.html', {'form': form})


@login_required
def article_summary(request):
    articles = Article.objects.prefetch_related('comments').all()  # Récupère tous les articles et leurs commentaires
    return render(request, 'article_summary.html', {'articles': articles})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()  # Supprime le commentaire
    return redirect('article_summary')  # Redirige vers la page des résumés après suppression





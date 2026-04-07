from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import InscriptionForm
from .models import Article
from .models import Article, Commentaire
from .forms import CommentaireForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'home.html')

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = InscriptionForm()

    return render(request, 'inscription.html', {'form': form})

def liste_article(request):
    article = Article.objects.all()
    context = {
        'articles' : article
    }
    return render(request, 'Article/liste_article.html', context)




def detail_article(request, id):
    article = get_object_or_404(Article, id=id)
    commentaires = article.commentaires.all() 

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentaireForm(request.POST)
            if form.is_valid():
                commentaire = form.save(commit=False)
                commentaire.auteur = request.user
                commentaire.article = article
                commentaire.save()
                return redirect('detail_article', id=article.id)
        else:
            return redirect('detail_article')
    else:
        form = CommentaireForm()

    context = {
        'article': article,
        'commentaires': commentaires,
        'form': form if request.user.is_authenticated else None
    }
    return render(request, 'Article/detail_article.html', context)
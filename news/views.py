from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import InscriptionForm
from .models import Article
from .forms import CommentaireForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import Commentaire

# Create your views here.

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render


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
    detail = get_object_or_404(Article, id=id)
    context = {
        'details' : detail
    }
    return render(request, 'Article/detail_article.html', context)

class LectureDetail(DetailView):
    model=Commentaire
    template_name='Article/lecture_detaille.html'

    
@login_required
def commentaire(request):
    if request.method=='POST':
        form=CommentaireForm(request.POST)
        if form.is_valid():
            form.save()
            print("Formulaire bien envoyé")
            form=CommentaireForm()
    else:
        form=CommentaireForm()
    context={
        'form':form
    }    
    return render(request,'Article/commentaire.html',context)

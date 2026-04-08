from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import InscriptionForm, CommentaireForm
from .models import Article, Commentaire
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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
    return render(request, 'home.html', context)




def detail_article(request, id):
    details = get_object_or_404(Article, id=id)
    commentaires = details.commentaires.all() 

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentaireForm(request.POST)
            if form.is_valid():
                commentaire = form.save(commit=False)
                commentaire.auteur = request.user
                commentaire.article = details
                commentaire.save()
                return redirect('detail_article', id=details.id)
        else:
            return redirect('detail_article')
    else:
        form = CommentaireForm()

    context = {
        'detail': details,
        'commentaires': commentaires,
        'form': form if request.user.is_authenticated else None
    }
    return render(request, 'Article/detail_article.html', context)


class CommentaireUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Commentaire
    fields = ['contenu']
    template_name = 'modifier_commentaire.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detail_article', kwargs={'id': self.object.article.id})

    def test_func(self):
        commentaire = self.get_object()
        return self.request.user == commentaire.auteur


class CommentaireDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Commentaire
    template_name = 'supprimer_commentaire.html'

    def get_success_url(self):
        return reverse_lazy('detail_article', kwargs={'id': self.object.article.id})

    def test_func(self):
        commentaire = self.get_object()
        return self.request.user == commentaire.auteur

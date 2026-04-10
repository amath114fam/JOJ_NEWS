from django.urls import path
from .views import home, inscription
from django.contrib.auth import views as auth_views
from . import views
from .views import CommentaireUpdateView, CommentaireDeleteView


urlpatterns = [
    path('', views.liste_article, name='home'),
    path('inscription/', inscription, name='inscription'),
    path('connexion/', auth_views.LoginView.as_view(template_name='connexion.html'), name='connexion'),
    path('deconnexion/', auth_views.LogoutView.as_view(next_page='home'), name='deconnexion'),

    path('motdepasseOUBLIER/',
         auth_views.PasswordResetView.as_view(template_name='motpasseOublier.html'),
         name='password_reset'),

    path('motdepasse-envoyer/',
         auth_views.PasswordResetDoneView.as_view(template_name='mailmotdepasse.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='nouveaumotpasse.html'),
         name='password_reset_confirm'),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='motpasseModifier.html'),
         name='password_reset_complete'),
      
    path('liste/', views.liste_article , name='liste_article'),
    path('Article/<int:id>/', views.detail_article , name='detail_article'),
    path('commentaire/<int:pk>/modifier/', CommentaireUpdateView.as_view(), name='modifier_commentaire'),
    path('commentaire/<int:pk>/supprimer/', CommentaireDeleteView.as_view(), name='supprimer_commentaire'),
]
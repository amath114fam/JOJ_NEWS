from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('inscription/', views.inscription, name='inscription'),

    path('connexion/', auth_views.LoginView.as_view(
        template_name='connexion.html'
    ), name='connexion'),

    path('deconnexion/', auth_views.LogoutView.as_view(
        next_page='home' ), name='deconnexion'),

    path('liste/', views.liste_article, name='liste_article'),
    path('article/<int:id>/', views.detail_article, name='detail_article'),
]
from django.urls import path
from .views import home, inscription
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('inscription/', inscription, name='inscription'),
    path('connexion/', auth_views.LoginView.as_view(template_name='connexion.html'), name='connexion'),
    path('deconnexion/', auth_views.LogoutView.as_view(next_page='home'), name='deconnexion'),
]
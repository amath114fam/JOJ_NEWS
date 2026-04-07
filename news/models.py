from django.db import models

from django.contrib.auth.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"


class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, related_name='articles')
    image = models.ImageField(upload_to='images/', blank=True, null=True) 

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-date_creation']

class Commentaire(models.Model):
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentaires')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaires')

    def __str__(self):
        return f"Commentaire de {self.auteur} sur {self.article}"

    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"
        ordering = ['-date_publication']
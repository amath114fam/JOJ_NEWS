
from django.contrib import admin
from .models import Categorie, Article, Commentaire

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'auteur', 'date_creation')
    list_filter = ('categorie', 'auteur', 'date_creation')
    search_fields = ('titre', 'contenu')
    readonly_fields = ('date_creation',)
    fieldsets = (
        ('Informations principales', {
            'fields': ('titre', 'categorie', 'auteur')
        }),
        ('Contenu', {
            'fields': ('contenu',)
        }),
        ('Dates', {
            'fields': ('date_creation',),
            'classes': ('collapse',)
        }),
        ('image',{
            'fields' : ('image',)
        }),
    )

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('auteur', 'article', 'date_publication')
    list_filter = ('article', 'auteur', 'date_publication')
    search_fields = ('contenu',)
    readonly_fields = ('date_publication',)
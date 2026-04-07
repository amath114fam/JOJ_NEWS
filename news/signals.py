from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .models import Commentaire

@receiver(post_save, sender=Commentaire)
def notifier_admin_nouveau_commentaire(sender, instance, created, **kwargs):
    if created:
        message = (
            f"Bonjour Administrateur,\n\n"
            f"Un nouveau commentaire a été posté.\n\n"
            f"Article : {instance.article.titre}\n"
            f"Auteur  : {instance.article.auteur}\n"
            f"Date    : {instance.article.date_creation}\n"
            f"Commentaire : {instance.article.contenu}\n\n"
            f"Cordialement,\n"
            f"JOJ News"
        )

        email = EmailMessage(
            subject=f'Nouveau commentaire sur : {instance.article.titre}',
            body=message,
            from_email=settings.ADMIN_EMAIL,
            to=[settings.ADMIN_EMAIL],
        )
        email.send()
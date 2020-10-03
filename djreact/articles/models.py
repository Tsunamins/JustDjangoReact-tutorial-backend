from django.db import models

# imports for django signals method of sending email on user creation
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.mail import send_mail


def welcome_user(sender, instance, **kwargs):
    if kwargs["created"]:
        new_user_email = instance.email
        new_username = instance.username
        url = 'http://127.0.0.1:8000/rest-auth/login/'
        subject = 'Welcome to the Wall'
        message = 'Welcome to the wall ' + new_username + ', \n' + 'Log in with the link below to start the Writing on the Wall. \n' + url
        send_mail(subject, message, from_email=None, recipient_list=[new_user_email], fail_silently=False, html_message=None)
        print(new_user_email + " from welcome user function")


post_save.connect(welcome_user, sender=User)


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title

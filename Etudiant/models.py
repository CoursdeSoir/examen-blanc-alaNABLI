from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser

import Etudiant

# Create your models here.
def verif_username(value):
    if not value.startswith('ing'):
        raise ValidationError({"username": ["Le nom d'utilisateur doit commence par 'ing'."]})
class Etudiant(AbstractUser):
    username = models.CharField(max_length=20, primary_key=True, validators=[verif_username])
    classe = models.CharField(max_length=8)
    email = models.EmailField('Email', max_length=50, unique=True)

    USERNAME_FIELD = 'username'
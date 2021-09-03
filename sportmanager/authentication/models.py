from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role_choices = (
      (0, 'admin'),
      (1, 'manager'),
    )

    role = models.PositiveSmallIntegerField(choices=role_choices, default=3)
    
    def __str__(self):
        if self.first_name and self.last_name:
            return '{} {}'.format(self.first_name, self.last_name)
        return self.email

    class Meta:
        verbose_name = 'Utente'
        verbose_name_plural = 'Utenti'


class ThemeConfig(models.Model):
    
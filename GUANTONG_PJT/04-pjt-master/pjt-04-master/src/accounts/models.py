from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    company_name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('user', 'company_name')
        
    def __str__(self):
        return f"{self.user.username} - {self.company_name}"

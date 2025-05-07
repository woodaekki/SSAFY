from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Create your models here.
class Stocks(models.Model):
    CompanyName = models.CharField(max_length=30)
    StockCode = models.CharField(max_length=6)
    Comments = models.TextField()
    StorageDate = models.DateTimeField(auto_now=True)

class CustomUserCreationForm(UserCreationForm) : 
    class Meta(UserCreationForm.Meta) : 
        model = get_user_model()
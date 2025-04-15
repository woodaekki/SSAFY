from django.db import models

# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model)    :
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    content = models.TextField()
from django.contrib import admin
# admin 모델 클래스 등록 (명시적 상대 경로)
from .models import Article

# Register your models here.
admin.site.register(Article)
from django.urls import path  # 여기서 path를 임포트합니다.
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
]

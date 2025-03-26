# from django.contrib import admin
from django.urls import path
from libraries import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('recommend/', views.recommend, name='recommend'),
    path('bestseller/', views.bestseller, name='bestseller'),
]
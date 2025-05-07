from django.urls import path
from . import views


app_name = "contentfetch"

urlpatterns = [
    path('index/', views.stock_finder, name='stock_finder'),
    path('delete_comment/', views.delete_comment, name='delete_comment'),
]
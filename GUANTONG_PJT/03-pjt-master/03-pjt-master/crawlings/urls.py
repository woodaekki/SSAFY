from django.urls import path
from . import views


app_name = 'crawlings'
urlpatterns = [
    path('', views.index, name='index'),
    path('search_page/<str:keyword>/', views.search_page, name = 'search_page'),
    path('delete_comment', views.delete_comment, name='delete_comment'),
    path('search/', views.search, name = 'search'),
]

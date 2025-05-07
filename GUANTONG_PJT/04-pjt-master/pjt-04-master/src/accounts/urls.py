from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('<int:user_pk>/', views.detail, name='detail'),
    path('addfavorites/', views.addfavorites, name='addfavorites'),
    path('delete_favorite/<int:pk>/', views.delete_favorite, name='delete_favorite'),
]

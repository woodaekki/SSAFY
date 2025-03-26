"""library_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from libraries import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index),
#     path('recommend/', views.recommend),
#     path('bestseller/', views.bestseller),
# ]

from django.contrib import admin
from django.urls import path, include  # include를 추가

# 'libraries.urls'를 include로 추가하여 urls.py 파일을 모듈화합니다.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('libraries.urls')),  # libraries.urls를 포함시킴
]


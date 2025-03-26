from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list_article(request):
    return render(request, "list_article.html")

def hello(request):
    return render(request, "hello.html")
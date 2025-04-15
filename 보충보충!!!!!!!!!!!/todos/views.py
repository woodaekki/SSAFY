from django.shortcuts import render
from .forms import TodoForm

# Create your views here.
def index(request):
    return render(request, 'todos/index.html')

def create(request):
    form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/create.html', context)

def update(request):
    pass

def delete(request):
    pass
from django.shortcuts import render, redirect
from .forms import DiaryForm, CommentForm
from .models import Diary, Comment

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    context = {
        'diaries': diaries
    }
    return render(request, 'diaries/index.html', context)

def create(request):
    if request.method == 'POST':
        # 빈폼을 보내서, 폼이 유효하면 저장해서 메인페이지에 띄워주고
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diaries:index')
        # 없으면 다시 빈폼 뿌리기 
    else:
        form = DiaryForm()
    context = {
        'form': form
    }
    return render(request, 'diaries/create.html', context)

def update(request, pk):
    # 사용자가 수정한걸 저장해서 인덱스에 띄워야겠지
    diary = Diary.objects.get(pk=pk)
    if request.method == 'POST':
        form = DiaryForm(request.POST, instance=diary)
        if form.is_valid():
            form.save()
        return redirect('diaries:index')
    else:
        # 이미 저장된걸 갖구오기
        # 근데 하나씩 갖구와야 하니까 pk 넘겨야겠지 
        form = DiaryForm(instance=diary)
    context = {
        'diary': diary,
        'form': form
    }
    return render(request, 'diaries/update.html', context)

def delete(request, pk):
    diary = Diary.objects.get(pk=pk)
    diary.delete()
    return redirect('diaries:index')

def detail(request, pk):
    diary = Diary.objects.get(pk=pk)
    form = CommentForm()
    context = {
        'diary': diary,
        'form': form
    }
    return render(request, 'diaries/detail.html', context)

def comment_create(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            
            return 


        
    return 

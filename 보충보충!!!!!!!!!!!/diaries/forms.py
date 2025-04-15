from .models import Diary, Comment
from django import forms

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
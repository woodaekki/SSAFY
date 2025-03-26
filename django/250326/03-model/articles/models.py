from django.db import models

# Create your models here.
# 게시글이 저장될 테이블을 설계하는 클래스
class Article(models.Model):
    title = models.CharField(max_length=10) # 제목 (제약조건: char은 길이 제한)
    content = models.TextField() # 내용 (text는 제한 없음)
    created_at = models.DateTimeField(auto_now_add=True) # 작성 시간 (처음 생성될때만 자동저장)
    updated_at = models.DateTimeField(auto_now=True) # 수정 시간 (수정할때마다 자동저장)

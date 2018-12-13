from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.CharField(max_length=120)   #CharField: 짧은 길이 텍스트
    title  = models.CharField(max_length=120)
    text   = models.TextField()  #TextField : 텍스트길이가 제한되어있지 않음
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True) #지금 시간을 자동으로 넣어줌

    def __str__(self):
        return self.title


class Page(models.Model):
    master = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MyPage(models.Model):
     master = models.CharField(max_length=120)
     name = models.CharField(max_length=120, default='홍길동')
     text = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     category= models.CharField(max_length=120)

     def __str__(self):
         return self.name



# 코멘트 모델



class Comment(models.Model):
     article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')  #Foreign키: 다른 모델에서 있는것도 사용가능/  (Article이라는 모델 클래스를 넣음), 글에서는 자기랑 연결된 글을 확인해보기 위해(comments(필드이름)) Article의 Comments라는 속성에 접근하면(양방향)
     author = models.CharField(max_length=120)
     text = models.TextField()
     password = models.CharField(max_length=120)
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return self.text






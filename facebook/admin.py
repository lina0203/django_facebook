from django.contrib import admin

# Register your models here.
from facebook.models import Article

admin.site.register(Article)

from facebook.models import Comment, MyPage
admin.site.register(MyPage)
admin.site.register(Comment)
1
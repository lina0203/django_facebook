"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path
from facebook.views import play
from facebook.views import play2,profile,event,fail,help,warn,seven,newsfeed,detail_feed,show,new_feed,edit_feed,remove_feed




urlpatterns = [
    path('admin/', admin.site.urls),
    path('play/',play),
    path('play2', play2),   #서버주소, 실행시키는 함수이름


                           # play2:
                          # 실행시키는 함수이름 from import play2인데
                          # facebook폴더안에 views.py파일로 들어가서 play2함수 실행
      path('woorina/profile/',profile),
      path('event/', event),
      path('fail/', fail),
      path('help/',help),
      path('warn/',warn),
      path('seven/',seven),
      path('/',newsfeed),
      path('feed/<pk>/',detail_feed),
      path('feed/<pk>/edit/',edit_feed),
      path('feed/<pk>/remove/',remove_feed),
      path('mypage/',show),
      path('new/',new_feed)

]


3


from django.shortcuts import render,redirect #render는 장고방식으로 / redirect는 요청한 주소로 보여줌
from facebook.models import Article,Comment
from facebook.models import MyPage


# Create your views here.

def play(request):
    name3 = '리나'
    return render(request, 'play.html',{'name5':name3})



count = 0
def play2(request):
    name = '우리나'     #텍스트는 따음표 써주기
    global count
    count = count +1

    age=22
    if age <19:
        status = '미성년자'
    else:
        status = '성인'

        diary = ['11월 22일','11월 23일','11월 24일']



    return render(request, 'play2.html', {'name':name, 'count':count, 'status':status, 'diary':diary})   #name이라는 값은 변수name을 읽어서 우리나를 띄어준다

def profile(request):
    return render(request, 'profile.html')


count=0
def event(request):
    global count
    count = count + 1

    if count!=7:
        status ='꽝입니다'

    else:
        status = '당첨입니다'
    return render(request, 'event.html',{'count':count,'status':status})

def fail(request):

    return render(request, 'fail.html')

def help(request):
    return render(request,'help.html')

def warn(request):
    return render(request,'warn.html')

def seven(request):

     num1=21
     num2=22
     if num1%7==0:
         status = str(num1) + '은 7의 배수입니다.'
     if num2%7!=0:
         status2 = str(num2) + '는 7의 배수가 아닙니다.'
     return render(request,'seven.html',{'status':status,'status2':status2})

def newsfeed(request):
    articles = Article.objects.all().order_by('-created_at')
    for article in articles:
        article.length = len(article.text)
    return render(request, 'newsfeed.html',{'articles':articles})

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method =='POST':
        Comment.objects.create(
            article = article,
            author = request.POST['nickname'],
            text = request.POST['reply'],
            password = request.POST['password']
        )
        return redirect(f'/feed/{article.pk}')
    return render(request, 'detail_feed.html',{'article':article}) #앞에 models.py에 related해줘서 다시 comments선언 안해도됨

def show(request):
    articles = MyPage.objects.all()

    return render(request, 'mypage.html', {'articles':articles})

def new_feed(request):

        #게시글이 등록되는 로직
        if request.method == 'POST':  # 폼이 전송되었을 때만 아래 코드를 실행


            new_article = Article.objects.create(    #새로 작성하는 create 씀( 저번시간은 get, all 씀(디비가져오기))
                author=request.POST['author'], #'author' ....author, title 저것들은 html에 적은 거랑 일치 해야함
                title=request.POST['title'],  #new_feed.html(name="author"...)에 입력한 값을 db에 넣어줌(89-92줄)
                password=request.POST['password'],
                text=request.POST['content']

            )  # 새글 등록 끝


            return redirect(f'/feed/{ new_article.pk}')  #새로 생긴 글에 pk를 지정해줌(85줄 변수로) 7번글을 만들면 new_article에서 7번째글을 만들고 그게 주소가 됨
                                                         #http://127.0.0.1:8000/feed/7/


        return render(request, 'new_feed.html')


def edit_feed(request,pk):
    article = Article.objects.get(pk=pk)


    if request.method == 'POST':
        if article.password == request.POST['password']:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save() #실행한 값이(값을 바꾸고 db에 저장됨)
            return redirect(f'/feed/{article.pk}')
        else:
            return redirect('/fail')
    return render(request, 'edit_feed.html', {'article': article})



def remove_feed(request,pk):   #삭제를 누르면 그 삭제페이지 주소를 받아온다
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if article.password == request.POST['password']:
            article.delete()

            return redirect('/')
        else:
            return redirect('/fail') #글 비밀번호 틀리게 입력하면 실패한 창(fail.html)이 뜸
    return render(request, 'remove_feed.html',{'article':article})
from django.shortcuts import render
from django.http import HttpResponse
from lotto.models import GuessNumbers
from lotto.forms import PostForm
# Create your views here.
def index(request) :
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos':lottos} )

def hello(request) :
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

def post(request) :
    print("*****************")
    print(request.method)
    print("*****************")

    if request.method == 'POST' :
        form = PostForm(request.POST)

        if form.is_valid():
            lotto = form.save(commit = False)# DB 저장은 아래 generate 함수의 . 로 처리
            lotto.generate()
            return redirect('index') # urls.py 의 name='index' 에 해당
            # --> 상단 from django.shortcuts import render, redirect 수정
    else:
        form = PostForm() # empty form
        return render(request, "lotto/form.html", {"form": form})


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey)
    return render(request, "lotto/detail.html", {"lotto":lotto})

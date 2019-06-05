from django.shortcuts import render
from .models import Board    # models.py 에 있는 Board 라는 class를 import 하겠다는 의미

def index(request):
    return render(request, 'boards/index.html') # templates 안의 boards 폴더에 있는 index.html을 랜더하겠다.

def new(request):
    return render(request, 'boards/new.html')

def create(request):
    title = request.GET.get('title')           # new.html 에서 가져온 title
    content = request.GET.get('content')

    # board = Board() # Board 라는 클래스에서 board라는 인스턴스 생성
    board = Board(title=title, content=content)
    board.save()

    return render(request, 'boards/create.html')

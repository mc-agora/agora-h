from django.shortcuts import render, redirect
from .models import Board    # models.py 에 있는 Board 라는 class를 import 하겠다는 의미

def index(request):
    boards = Board.objects.all()[::-1]
    context = {'boards': boards}
    return render(request, 'boards/index.html', context) # templates 안의 boards 폴더에 있는 index.html을 랜더하겠다.

def new(request):
    return render(request, 'boards/new.html')

def create(request):
    title = request.POST.get('title')     # new.html 에서 가져온 title
    content = request.POST.get('content')
    # board = Board() # Board 라는 클래스에서 board라는 인스턴스 생성
    board = Board(title=title, content=content)
    board.save()
    return redirect(f'/boards/{board.pk}/')

def detail(request, pk):
    board = Board.objects.get(pk=pk)     # pk를 조건으로 가져옴
    context = {'board': board}
    return render(request, 'boards/detail.html', context)

def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('/boards/')

def edit(request, pk):
    board = Board.objects.get(pk=pk)
    context = {'board': board}
    return render(request, 'boards/edit.html', context)

def update(request, pk):
    board = Board.objects.get(pk=pk)
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect(f'/boards/{board.pk}/')


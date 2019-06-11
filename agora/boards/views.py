from django.shortcuts import render, redirect
from .models import Board, Comment    # models.py 에 있는 Board 라는 class를 import 하겠다는 의미

def index(request):
    boards = Board.objects.all()[::-1]
    context = {'boards': boards}
    return render(request, 'boards/index.html', context) # templates 안의 boards 폴더에 있는 index.html을 랜더하겠다.

def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')  # new.html 에서 가져온 title
        content = request.POST.get('content')
        # board = Board() # Board 라는 클래스에서 board라는 인스턴스 생성
        board = Board(title=title, content=content)
        board.save()
        return redirect('boards:index')
    else:
        return render(request, 'boards/new.html')

def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)     # pk를 조건으로 가져옴
    comments = board.comment_set.all()
    context = {'board': board, 'comments': comments}
    return render(request, 'boards/detail.html', context)

def delete(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)

def edit(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        context = {'board': board}
        return render(request, 'boards/edit.html', context)

<<<<<<< HEAD
def update(request, pk):
    board = Board.objects.get(pk=pk)
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect(f'/boards/{board.pk}/')

=======
def comments_create(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        comment = Comment()
        comment.board_id = board.pk
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('boards:detail', board.pk)
    else:
        return redirect('boards:detail', board.pk)
>>>>>>> 9f43753a3e16e038989e28ea992d0563c821ece3

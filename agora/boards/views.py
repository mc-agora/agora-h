from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Comment    # models.py 에 있는 Board 라는 class를 import 하겠다는 의미
from .forms import BoardForm, CommentForm
from django.core.paginator import Paginator # paging 을 하기 위해 사용
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def index(request):
    boards = Board.objects.all()[::-1]
    paginator = Paginator(boards, 5) # 한 페이지당 5개의 글을 보여주겠다
    page = request.GET.get('page')
    lists = paginator.get_page(page)
    context = {'boards': boards, 'lists': lists}
    return render(request, 'boards/index.html', context) # templates 안의 boards 폴더에 있는 index.html을 랜더하겠다.

@login_required() # 로그인한 사람만 글을 쓸 수 있도록
def new(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():  # 유효성 검사
            board = form.save(commit=False)   # 잠시 저장되지 않게 함
            board.user = request.user
            board.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm()
    context = {'form': form}
    return render(request, 'boards/form.html', context)

def detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    comments = board.comment_set.all()
    comment_form = CommentForm()
    context = {
        'board': board,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'boards/detail.html', context)


def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if board.user == request.user:  # 작성한 유저와 삭제요처을 한 유저가 같으면 조건문 실행
        if request.method == 'POST':
            board.delete()
            return redirect('boards:index')
        else:
            return redirect('boards:detail', board.pk)
    else:
        return redirect('boards:index')

@login_required()
def edit(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if board.user == request.user:
        if request.method == 'POST':
            form = BoardForm(request.POST, instance=board)
            if form.is_valid():
                form.save()
                return redirect('boards:detail', board.pk)
        else:
            form = BoardForm(instance=board)
    else:
        return redirect('boards:index')
    context = {'board': board, 'form': form}
    return render(request, 'boards/form.html', context)


@login_required()
@require_POST   # POST 요청을 제외한 요청이 들어오면 405 에러가 뜬다
def comments_create(request, board_pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.board_id = board_pk
        comment.save()
    return redirect('boards:detail', board_pk)

@login_required()
def comments_edit(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('boards:detail', board_pk)
        else:
            form = CommentForm(instance=comment)
    else:
        return redirect('boards:detail', board_pk)
    context = {'form': form, 'comment': comment}
    return render(request, 'boards/comment_edit.html', context)

@login_required()
@require_POST
def comments_delete(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user != comment.user:
        return redirect('boards:detail', board_pk)
    comment.delete()
    return redirect('boards:detail', board_pk)

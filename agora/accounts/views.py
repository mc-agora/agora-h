from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash # 비밀번호를 변경해도 로그인 상태 유지
from .forms import UserCustomCreationForm, UserCustomChangeForm
from IPython import embed

def signup(request):
    if request.user.is_authenticated:             # 만약 로그인이 된 상태이면 바로 index 페이지로 보내버림
        return redirect('parsed_data:index')
    if request.method == 'POST':
        form = UserCustomCreationForm(request.POST, request.FILES)
        #embed()
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('parsed_data:index')
    else:
        form = UserCustomCreationForm()
    context = {'form': form}
    return render(request, 'accounts/auth_form.html', context)

def login(request):
    if request.user.is_authenticated:             # 만약 로그인이 된 상태이면 바로 index 페이지로 보내버림
        return redirect('parsed_data:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        embed()
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'parsed_data:index')
    else:
        form = AuthenticationForm()
    context ={'form': form}
    return render(request, 'accounts/auth_form.html', context)

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('parsed_data:index')
    else:
        return redirect('parsed_data:index')

def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('parsed_data:index')
    else:
        return redirect('parsed_data:index')

def edit(request):
    if request.method == 'POST':
        form = UserCustomChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('parsed_data:index')
    else:
        form = UserCustomChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'accounts/auth_form.html', context)

# 190619 추가
def change_password(request):
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)   # 비밀번호가 변경되어도 '나'라고 알림
        form.save()
        return redirect('parsed_data:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'accounts/auth_form.html', context)

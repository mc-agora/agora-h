from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


### 자신의 페이지
@login_required()
def userprofile(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)

    if not person.profilepic:
        pic_url = ""
    else:
        pic_url = person.profilepic.url
    context = {
        'id': person.username,
        'name': person.user_name,
        'birthdate': person.birthdate,
        'job': person.job,
        'age': person.age,
        'gender': person.gender,
        'pic': pic_url
    }
    return render(request, 'mypage/userprofile.html', context)



from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect


# Create your views here.


def index_view(request):
    if request.user.is_authenticated: # 로그인이 완료 됬다면.
        return redirect('main:index_after')
    else:
        return render(request, 'main/index.html')


def index_after_view(request):
    return render(request, 'main/index_after.html')


def logout_btn(request):
    logout(request)
    return redirect('main:index')

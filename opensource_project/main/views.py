from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from .models import Photo

# Create your views here.


def index_view(request):
    if request.user.is_authenticated: # 로그인이 완료 됬다면.
        return redirect('main:mainpage')
    else:
        return render(request, 'main/index.html')


def mainpage_view(request):
    if request.user.is_authenticated is None:  # 로그인확인
        return redirect('main:index')
    print(request.user.username)
    return render(request, 'main/mainpage.html')


def showpage_view(request):
    if request.user.is_authenticated is None:  # 로그인확인
        return redirect('main:index')
    if request.method == 'POST':
        myimage = request.FILES.get('uploadImage')
        if myimage is not None:
            name = request.user.username
            image = Photo()
            image.email = request.user.email
            image.image = myimage
            image.save()
            return render(request, 'main/showpage.html', {'myImage': image, 'Username': name})
        else:
            redirect('main:mainpage')

    return redirect('main:mainpage')


def logout_btn(request):
    logout(request)
    return redirect('main:index')

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

def mypage_view(request):
    if request.user.is_authenticated is None:  # 로그인확인
        return redirect('main:index')
    if request.method == 'GET':
        user = request.user
        myimages = Photo.objects.order_by('-created_at') #최신순 정렬, 배열로 넘어옴
        print(myimages)
        if myimages is not None: # 사진 유무 파악
            image = myimages[0]  # 젤 첫번째 사진
            return render(request, 'main/mypage.html', {'bool': True, 'image': image, 'user': user})
        else :
            image = ""
            return render(request, 'main/mypage.html', {'bool': False, 'image': image, 'user': user})



def delete_photo(request,pid):
    curphoto = Photo.objects.get(id=pid)
    curphoto.delete()
    return redirect('main:mypage')

def logout_btn(request):
    logout(request)
    return redirect('main:index')

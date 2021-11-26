from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('mainpage', views.mainpage_view, name='mainpage'),
    path('showpage', views.showpage_view, name='showpage'),
    path('logout', views.logout_btn, name='logout'),
    path('mypage', views.mypage_view, name='mypage'),
    path('mypage/<int:pid>/delete_photo',views.delete_photo, name='mypagedelete')
]

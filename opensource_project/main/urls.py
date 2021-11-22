from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('mainpage', views.mainpage_view, name='mainpage'),
    path('showpage', views.showpage_view, name='showpage'),
    path('logout', views.logout_btn, name='logout'),
]

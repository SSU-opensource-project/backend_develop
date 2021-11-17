from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('index_after', views.index_after_view, name='index_after'),
    path('logout', views.logout_btn, name='logout')
]
from django.urls import path
from . import views

app_name='music'

urlpatterns = [
    path('music/', views.index, name='views'),
    path('', views.second_page, name='second-page'),
    path('music/<int:album_id>', views.detail, name='detail'),
    path('music/<int:album_id>/favourite', views.favourite, name='favourite')
]
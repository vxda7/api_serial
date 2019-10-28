from django.urls import path
from . import views

app_name='musics'


urlpatterns = [
    path('musics/', views.music_list, name="music_list"),
    path('musics/<int:id>/', views.music_detail, name="music_detail"),
    path('artists/', views.artist_list, name="artist_list"),
    path('artists/<int:id>/', views.artist_detail, name="artist_detail"),
    path('musics/<int:id>/comments/', views.comment_create, name="comment_create"),
    path('comments/<int:id>/', views.comment_detail, name="comment_detail")
]
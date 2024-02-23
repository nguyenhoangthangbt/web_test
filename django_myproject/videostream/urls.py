from django.urls import path
from .views import stream_video, video_player, upload_video

urlpatterns = [
    path('<int:video_id>/', stream_video, name='stream_video'),
    path('player/', video_player, name='video_player'),
    path('upload/', upload_video, name='upload_video'),
]

from django.http import HttpResponse, FileResponse,HttpRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Video
from .forms import VideoForm
from django.shortcuts import render,redirect

ALLOWED_CLIENT_ADDR =['10.0.0.5', '127.0.0.1', 'localhost']
@login_required
def stream_video(request: HttpRequest, video_id: int):
    # Check if the request is internal
    client_ip = request.META.get('REMOTE_ADDR')
    print("cur_HOST = ",request.get_host())
    print("client_ip = ",client_ip)

    if client_ip not in ALLOWED_CLIENT_ADDR:
        # If the request is external, return a permission denied response
        return HttpResponse('Permission denied', status=403)
    
    # If the request is internal, proceed to stream the video
    video = get_object_or_404(Video, pk=video_id)
    video_path = video.file.path
    return FileResponse(open(video_path, 'rb'), content_type='video/mp4')


@login_required
def video_player(request):
    videos = Video.objects.all()
    return render(request, 'videostream/video_player.html', {'videos': videos})

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_player')
    else:
        form = VideoForm()
    return render(request, 'videostream/upload_video.html', {'form': form})

from django.shortcuts import render
from .models import Item
from django.http import HttpResponseNotFound,HttpResponse
from django.http import FileResponse
import os
# from django.shortcuts import STATIC_ROOT

def item_list(request):
    items = Item.objects.all()
    return render(request, 'myapp/item_list.html', {'item_list': items})

def video_view1(request):
    # Construct the file path to the video file
    video_file_path = 'assets/media2/clip2.mp4'
    # Serve the video file using Django's FileResponse
    return FileResponse(open(video_file_path, 'rb'))
from django.contrib.auth.decorators import login_required
@login_required
def video_page(request):
    # Path to the video file
    video_file_path = 'assets/media2/clip2.mp4' #'assets/media2/photo1.jpg'#'

    # Check if the file exists
    if os.path.exists(video_file_path):
        # Serve the video file using FileResponse
        video_response = FileResponse(open(video_file_path, 'rb'))#, content_type='video/mp4')
        # Render the HTML page containing the video iframe
        video_rendered = render(request, 'myapp/view_video2.html', {'video_response': video_response})
        return video_response # video_rendered#video_response#
    else:
        # Return 404 if the file does not exist
        return HttpResponseNotFound("Video not found")

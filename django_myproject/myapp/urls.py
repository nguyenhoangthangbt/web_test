from django.urls import path
from . import views,models

urlpatterns = [
    path('',views.item_list),
    path('video/',views.video_view1),
    # path(route='video2/',view=views.video_view2,name='video_view2'),
    path(route='video2/',view=views.video_page,name='video_page'),
    
    
]

from django.urls import path
from . import views

urlpatterns=[
    path('get_schedule/', views.FetchScheduleView.as_view(), name='get_schedule'),
    path('update_schedule/', views.UpdateScheduleView.as_view(), name='update_schedule'),
    path('upload_schedule/', views.UploadScheduleView.as_view(), name='upload_schedule'),
]

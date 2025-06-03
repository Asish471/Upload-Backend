from django.urls import path
from .views import FileUploadView,FileListView,DownloadFileView
# from.views import FileListAPIView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='upload'),
    path('files/', FileListView.as_view(), name='file-list'),
    # path('download/', download_file, name='download_file'),
    path('download/<int:pk>/', DownloadFileView.as_view(), name='download-file'),
]

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .models import UploadedFile,MyFile
from .serializers import UploadedFileSerializer
from django.conf import settings
import os
import mimetypes
from django.http import FileResponse,HttpResponse,JsonResponse
from django.http import FileResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('files')  # get multiple files from "files" key
        uploaded = []

        for file in files:
            serializer = UploadedFileSerializer(data={'file': file})
            if serializer.is_valid():
                serializer.save()
                uploaded.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'uploaded': uploaded}, status=status.HTTP_201_CREATED)
    
    
# class FileListAPIView(APIView):
#     def get(self, request):
#         upload_path = os.path.join(settings.MEDIA_ROOT, 'uploads')
#         files = []
#         if os.path.exists(upload_path):
#             for fname in os.listdir(upload_path):
#                 files.append({
#                     "name": fname,
#                     "url": f"{settings.MEDIA_URL}uploads/{fname}"
#                 })
#         return Response(files)


class FileListView(APIView):
    def get(self, request):
        files = UploadedFile.objects.all()
        serializer = UploadedFileSerializer(files, many=True)
        return Response(serializer.data)


class DownloadFileView(APIView):
    # def get(self, request, pk):
    #     try:
    #         file_obj = UploadedFile.objects.get(pk=pk)
    #         # response = FileResponse(file_obj.file.open(), as_attachment=True, filename=file_obj.file.name)
    #         # return response
            
            # return Response({
            #     "file_name": file_obj.file.name.split('/')[-1],
            #     "file_url": request.build_absolute_uri(file_obj.file.url)
            # })
    #     except UploadedFile.DoesNotExist:
    #         raise Http404("File not found")contenttype application/pdf
    
    # def get(request, file_id,pk):
    #     file_obj = UploadedFile.objects.get(pk=pk)
    #     file_path = file_obj.file.path
    #     file_name = os.path.basename(file_path)
    #     content_type, _ = mimetypes.guess_type(file_path)

    #     # response = FileResponse(open(file_path, 'rb'), as_attachment=True,filename=file_name, content_type=content_type)
    #     response = FileResponse(open(file_path, 'rb'), content_type=content_type)
    # # Use this line for ASCII-safe filenames:
    # response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    #     print("response",response)
    #     response['Content-Length'] = os.path.getsize(file_path)
    #     return response
    
    
    # def get(request, file_id, pk):
    #     file_obj = UploadedFile.objects.get(pk=pk)
    #     file_path = file_obj.file.path
    #     print("filepath",file_path)
    #     file_name = os.path.basename(file_path)
    #     content_type, _ = mimetypes.guess_type(file_pacontenttype application/pdfth)

    #     response = FileResponse(open(file_path, 'rb'), content_type=content_type)
    #     response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    #     # Or this line for Unicode-safe filenames:
    #     # response['Content-Disposition'] = f"attachment; filename*=UTF-8''{quote(file_name)}"
        
    #     response['Content-Length'] = os.path.getsize(file_path)
    #     print(response)
    #     return response
    
    
    def get(request, file_id, pk):
        file_obj = UploadedFile.objects.get(pk=pk)
        file_path = file_obj.file.path
        file_name = os.path.basename(file_path)
        
        content_type, _ = mimetypes.guess_type(file_path)
        print("contenttype",content_type)
        content_type = content_type or 'application/octet-stream'

        with open(file_path, 'rb') as f:
            file_data = f.read()

        response = FileResponse(file_data, content_type=content_type,as_attachment=False)
        
        # response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        response['Content-Length'] = os.path.getsize(file_path)
        
        # response['X-Filename'] = file_name
        print("response",response)
        return response
    
    
    
   
    
    
    
    

# def force_download(request, filename):
#     file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', filename)
#     if os.path.exists(file_path):
#         return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
#     else:
#         raise Http404("File not found")


# @csrf_exempt
# def download_file(request):
#     filename = request.GET.get('filename')
#     if not filename:
#         raise Http404("Filename parameter missing")

#     # Sanitize filename to avoid directory traversal
#     filename = filename.lstrip('/')

#     file_path = os.path.join(settings.MEDIA_ROOT, filename)
#     if os.path.exists(file_path):
#         response = FileResponse(open(file_path, 'rb'), content_type='application/octet-stream')
#         response['Content-Disposition'] = f'attachment; filename="{os.path.basename(filename)}"'
#         return response
#     else:
#         raise Http404("File not found")
    

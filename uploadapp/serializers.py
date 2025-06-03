from rest_framework import serializers
from .models import UploadedFile,MyFile

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = '__all__'


class MyFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyFile
        fields = ['id', 'name', 'file']
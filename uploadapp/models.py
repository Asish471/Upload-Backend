from django.db import models
import os

# Create your models here.


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.file.name


class MyFile(models.Model):
    name=models.CharField(max_length=100)
    file=models.FileField(upload_to='uploads/')
    
    
    
    def delete(self, *args, **kwargs):
        # delete the file from disk
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super().delete(*args, **kwargs)
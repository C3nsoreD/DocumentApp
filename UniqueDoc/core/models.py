from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)

class Document(models.Model):
    description = models.CharField(max_length=100)
    file = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

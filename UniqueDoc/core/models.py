from django.db import models

# from Auth.models import User

# Create your models here.

def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)

class Document(models.Model):
    user_id = models.ForeignKey('Auth.User', on_delete=models.CASCADE)

    description = models.CharField(max_length=100)
    file = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File {file.name} with size {file.size}"

    def get_meta_data(self):
        pass


class DocumentInfo(models.Model):
    pass

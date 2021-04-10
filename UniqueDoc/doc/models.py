from django.db import models

# from Auth.models import User

# Create your models here.

def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)

# Document classification necessary for additional functionality
DOC_CLASS = [
    ('F', 'formal'),
    ('INF', 'informal')
]

class Document(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=100)
    classification = models.CharField(max_length=3, choices=DOC_CLASS, default='INF')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/')

    # user_id = models.ForeignKey('Auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"File {file.name} with size {file.size}"

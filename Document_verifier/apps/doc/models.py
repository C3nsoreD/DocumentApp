from django.db import models
from django.urls import reverse

# from Auth.models import User

# Create your models here.

def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)

# Document classification necessary for additional functionality
class ClassificationManager(models.Manager):

    def get_queryset(self, certification="unofficial"):
        return super(ClassificationManager, self).get_queryset().filter(status=certification)

class Document(models.Model):
    DOC_CLASS = [
        ('official', 'Official'),
        ('unofficial', 'Unofficial')
    ]
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, default='')
    uploaded_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='uploads/')

    certification = models.CharField(max_length=10, choices=DOC_CLASS, default='unofficial')

    owner_id = models.ForeignKey('Auth.User', on_delete=models.CASCADE, related_name='documents')

    objects = models.Manager()
    classification = ClassificationManager()

    class Meta:
        ordering = ('-uploaded_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('apps.doc:doc', args=[self.objects.title])

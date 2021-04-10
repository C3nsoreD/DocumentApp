from django.urls import path

from . import views

app_name = 'apps.doc'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('upload/', views.upload_document, name='upload'),
    path('document/', views.view_document, name='view-document'),
]

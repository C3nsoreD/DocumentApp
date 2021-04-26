from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'apps.doc'

urlpatterns = [
    path('', views.index, name='index'),
    # path('', TemplateView.as_view(template_name='doc/index.html')),
    path('upload/', views.upload_document, name='upload'),
    path('document/<title>/', views.document_detail_view, name='document_detail_view'),
    path('documents/', views.document_list_view, name='document_list_view'),

]

import io
from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, FileResponse
from django.core.files.storage import FileSystemStorage
from reportlab.pdfgen import canvas

from .forms import DocumentForm
from .utils.storage import CustomStorage
from .models import Document


# helper function for collecting serverside cookie.
def get_serverside_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_counter(request):
    # gets the cookie value `visits` if it exists otherwise sets the default to 1
    visits = int(get_serverside_cookie(request, 'visits', '1'))
    # gets the cookie value `last_visit` if it exists otherwise sets the default to datetime.now()
    last_visit_cookie = get_serverside_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).seconds > 10:
        visits += 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits

def index(request):
    context = {}
    visitor_cookie_counter(request)
    context['visits'] = request.session['visits']
    return render(request, 'doc/index.html', context)

def upload_document(request):
    context = {}
    if request.method == 'POST' and request.FILES['fileobj']:
        # form = DocumentForm()
        # if request.user.is_authenticated:
        form = DocumentForm(request.POST, file=request.FILES['fileobj'])
        if form.is_valid():
            # Save the file
            messages.info(request, 'File uploaded successfully.')
            form.save()
            print(request)
        else:
            form = DocumentForm()
        context['form'] = form
    # print(request)
    return render(request, 'doc/upload-doc.html', context)

def document_list_view(request):
    docs = Document.objects.all()
    return render(request, 'doc/list.html', {'docs': docs})

def document_detail_view(request, title):
    doc = get_object_or_404(Document, title=title)
    return render(request, 'doc/detail.html', {'doc': doc})

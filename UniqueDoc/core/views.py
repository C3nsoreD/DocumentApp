from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from .forms import DocumentForm
from .utils.storage import CustomStorage


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
    context_dict = {}
    # request.set_test_cookie()
    visitor_cookie_counter(request)
    context_dict['visits'] = request.session['visits']

    if request.method == 'POST' and request.FILES['fileobj']:
        if request.user.is_authenticated:
            form = DocumentForm(request.POST, file=request.FILES['fileobj'])
            # file_obj = request.FILES['fileobj']

        # fs = FileSystemStorage()
        # fs.save(file_obj.name, file_obj)
        # uploaded_file_url = fs.url
        # print(request)
        #
        # context_dict['uploaded_file_url'] = uploaded_file_url
        #
        # return render(request, 'core/index.html', context_dict)
        # custom_fs = CustomStorage(file_obj)
        # uploaded_file_url = custom_fs.
        if form.is_valid():
            form.save()
            print(request)
    else:
        form = DocumentForm()
    context_dict['form'] = form
    # response = render(request, 'core/index.html', context_dict)
    return render(request, 'core/index.html', context_dict)

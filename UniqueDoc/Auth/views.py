from django.shortcuts import render


from .models import User
from .forms import UserForm

# Create your views here.
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        # Check if the form is valid
        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request,
        'Auth/register.html',
        {'user_form': user_form,
        'registered': registered}
    )

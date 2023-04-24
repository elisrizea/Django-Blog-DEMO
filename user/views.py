from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserRegForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        rergform = UserRegForm(request.POST)
        if rergform.is_valid():
            rergform.save()
            usename = rergform.cleaned_data.get('username')
            messages.success(request, usename)
            status = ' Username added to the dayabase'
            return redirect('login')
        else:
            messages.error(request,f'error')
            status=' Username already exist in the database'
            rergform = UserRegForm()
            return render(request, 'register.html', {"rergform": rergform,"status":status})


    else:
        rergform = UserRegForm()
        return render(request, 'register.html', {"rergform": rergform})




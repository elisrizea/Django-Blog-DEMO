from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def support(request):
    s='form'
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["alin.rizea@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            s = "success"
    return render(request, "contact.html", {"form": form, 's':s})

def successView(request):
    return HttpResponse("Success! Thank you for your message.")
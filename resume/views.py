from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Message Sent...")
      return redirect("index")
  form = ContactForm()
  context = {"form" : form}
  return render(request, "resume/index.html", context )

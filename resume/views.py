from django.shortcuts import render, redirect
from .forms import BioForm, SkillsForm
from .models import Bio
# Create your views here.

def index(request):
  if request.method == "POST":
    form = BioForm(request.POST)
    if form.is_valid():
      form.save()
      print("Form saved..")
      return redirect("index")
  form = BioForm()
  context = {"form" : form}
  return render(request, "resume/index.html", context )

def add_skills(request):
  if request.method == "POST":
    form = SkillsForm(request.POST)
    if form.is_valid():
      form.save()
      print("Saved...")
      return redirect("/")
  form = SkillsForm()
  context = {"form" : form}
  return render(request, "resume/sample.html", context)
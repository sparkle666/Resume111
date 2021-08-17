from django import forms

from .models import Bio, Skills

class BioForm(forms.ModelForm):
  class Meta:
    model = Bio
    fields = "__all__"

class SkillsForm(forms.ModelForm):
  class Meta:
    model = Skills
    fields = "__all__"


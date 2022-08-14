from django import forms
from wanted.models import Company

class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['position','money','detail','skill']
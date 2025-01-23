# forms.py

from django import forms
from .models import Complaints

class ComplaintForm(forms.Form):
    cat_id = forms.IntegerField()
    subcategory_id = forms.IntegerField()
    complainttype = forms.ChoiceField(choices=[('Complaint', 'Complaint'), ('General Query', 'General Query')])
    stateid = forms.IntegerField()
    noc = forms.CharField(max_length=255)
    complaindetails = forms.CharField(widget=forms.Textarea, max_length=2000)
    compfile = forms.FileField(required=False)

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ['cat_id', 'subcategory_id', 'complainttype', 'stateid', 'noc', 'complaindetails', 'compfile']
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.extras.widgets import SelectDateWidget


class RevenueForm(forms.Form):
    start_date = forms.DateField(required=True, widget=SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ))
    end_date = forms.DateField(required=True, widget=SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ))

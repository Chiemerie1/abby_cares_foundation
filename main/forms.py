from django import forms

from .models import VolunteerContact


class VolunteerContactForm(forms.ModelForm):
    class Meta:
        model = VolunteerContact
        fields = "__all__"
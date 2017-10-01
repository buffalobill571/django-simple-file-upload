from django import forms
from generate_qrcode.models import Some


class SomeForm(forms.ModelForm):
    class Meta:
        model = Some
        fields = ['name', 'image']

from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Library

class LibraryForm(forms.ModelForm):
    image = CloudinaryFileField()
    class Meta: 
        model = Library
        fields = ['image']
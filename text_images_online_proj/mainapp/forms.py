
# import form class from django
from django import forms
 
# import GeeksModel from models.py
from .models import ImageModel
 
# create a ModelForm
class ImageForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = ImageModel
        fields = ('title', 'image')

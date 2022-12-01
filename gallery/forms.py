from django import forms
from django.forms import DateInput

from gallery.models import Gallery_Model




class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery_Model
        fields = ('title','image','contents')

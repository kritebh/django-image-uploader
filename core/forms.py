from .models import ImageUpload
from django import forms

class UploadImage(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = '__all__'
        labels = {'image':''}
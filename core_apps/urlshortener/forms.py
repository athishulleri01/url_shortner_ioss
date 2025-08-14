from django import forms
from .models import URL

class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['original_url']
        widgets = {
            'original_url': forms.URLInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter your long URL here...',
                'required': True,
            })
        }
    
    def clean_original_url(self):
        url = self.cleaned_data['original_url']
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        return url

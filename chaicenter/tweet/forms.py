from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        # widgets = {
        #     'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'What\'s happening?'})  # Placeholder for the text area
        # }
        # labels = {
        #     'text': '',  # No label for the text area
        #     'photo': 'Upload a photo'  # Label for the photo upload field
        # }
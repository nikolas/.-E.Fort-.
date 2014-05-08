from django import forms

from .models import Thumper

class ThumperForm(forms.ModelForm):
    class Meta:
        model = Thumper
        fields = ['author', 'content', 'image']

    def clean(self):
        cleaned_data = super(ThumperForm, self).clean()
        if (not cleaned_data['content'] and not cleaned_data['image']):
            raise forms.ValidationError("Form has no content.")
        return cleaned_data

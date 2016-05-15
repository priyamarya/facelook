from django import forms
from .models import Cards


class CardsForm(forms.ModelForm):

    class Meta:
        model = Cards
        fields = ["name", "image", "desc"]

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     return name

    # def clean_image(self):
    #     image = self.cleaned_data.get('image')
    #     return image

    # def clean_desc(self):
    #     desc = self.cleaned_data.get('desc')
    #     return desc

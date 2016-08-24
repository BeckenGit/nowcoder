from django import forms
class TextClassifierForm(forms.Form):
    text = forms.CharField(label='Enter your text', max_length=1000)

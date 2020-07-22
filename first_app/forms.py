from django import forms

class FormName(forms.Form):
        name = forms.CharField(validators=[check_for_z])
        email = forms.EmailField()
        text = forms.CharField(widget=forms.Textarea)
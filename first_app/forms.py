from django import forms
from first_app.models import Employee

class EmployeeForm(forms.ModelForm):
        class Meta:
                model = Employee
                # fields = "__all__"
                fields = ['first_name', 'last_name', 'email', 'contact']


class Subscribe(forms.Form):
        Email = forms.EmailField()

        def __str__(self):
                return self.Email
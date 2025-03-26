from django import forms
from django.forms import Form

class GeneratorForm(Form):
    count_symbol = forms.CharField(
        label='Count Symbols',
        initial=12,
        widget=forms.TextInput(attrs={
            'type':'number',
            'id': 'countSymbols',
            'placeholder':'count symbols',
            'aria-describedby': 'countSymbolsHelp',
            'class':'form-control text-capitalize p-2',
            'required': ''
        })
    )

    show_password = forms.CharField(
        label='Your Password',
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'id':'ShowPassword',
                'placeholder': 'your password',
                'class': 'show-password form-control text-capitalize p-2',
                'readonly':''
            }
        )
    )

class ExportFormatForm(forms.Form):
    FORMAT_CHOICES = [
        ('csv', 'csv'),
        ('json', 'json'),
        ('pdf', 'pdf'),
    ]

    file_format = forms.ChoiceField(
        choices=FORMAT_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
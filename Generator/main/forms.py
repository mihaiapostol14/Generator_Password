from django import forms
from django.forms import Form

class GeneratorForm(Form):
    count_symbol = forms.IntegerField(
        label='Count Symbols',
        label_suffix='',
        initial=12,
        min_value=12,
        max_value=120,
        widget=forms.NumberInput(attrs={
            'id': 'countSymbols',
            'placeholder': 'count symbols',
            'aria-describedby': 'countSymbolsHelp',
            'class': 'form-control text-capitalize p-2',
            'required': ''
        })
    )


    show_password = forms.CharField(
        label='Your Password',
        label_suffix='',
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
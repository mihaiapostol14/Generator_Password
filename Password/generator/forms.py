from django.core.exceptions import ValidationError
from django.forms import Form
from django import forms


class GeneratorForm(Form):
    length = forms.IntegerField(
        label="Password Length",
        min_value=6,
        max_value=500,
        initial=12,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter password length"
            }
        )
    )

    uppercase = forms.BooleanField(
        required=False,
        initial=True,
        label="Uppercase Letters (A-Z)",
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input"}
        )
    )

    lowercase = forms.BooleanField(
        required=False,
        initial=True,
        label="Lowercase Letters (a-z)",
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input"}
        )
    )

    numbers = forms.BooleanField(
        required=False,
        initial=True,
        label="Numbers (0-9)",
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input"}
        )
    )

    symbols = forms.BooleanField(
        required=False,
        label="Symbols (!@#$)",
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input"}
        )
    )

    def clean(self):
        self.cleaned_data = super().clean()
        check_fields = [*self.base_fields.keys()][1:]
        checkbox_values = []

        for field_name in check_fields:
            value = self.cleaned_data.get(field_name)
            checkbox_values.append(value)

            if not any(checkbox_values):
                raise ValidationError(f'Please Select {' or '.join(check_fields)}')
        return self.cleaned_data


class ExportFormatForm(Form):
    CHOICE_FORMAT = [
        ('csv', 'CSV'),
        ('txt', 'TXT'),
        ('json', 'JSON'),
    ]

    file_format = forms.ChoiceField(
        choices=CHOICE_FORMAT,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

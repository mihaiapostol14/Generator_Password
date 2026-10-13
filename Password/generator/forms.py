from django import forms
from django.forms import Form


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
        """
        Custom validation method to clean and verify form data.
        Ensures proper length constraints and guarantees that
        at least one character set checkbox is checked.
        """
        cleaned_data = super().clean()

        # 1. Safely retrieve and validate the password length
        length = cleaned_data.get('length')
        if length is not None:
            if length < 1 or length > 500:
                self.add_error('length', 'Password length must be between 1 and 500.')

        # 2. Explicitly fetch checkbox states by their field names
        # (Replace these keys with your actual form field names if they differ)
        use_upper = cleaned_data.get('uppercase', False)
        use_lower = cleaned_data.get('lowercase', False)
        use_digits = cleaned_data.get('digits', False)
        use_symbols = cleaned_data.get('symbols', False)

        # 3. Flexible check: allow any combination of checkboxes,
        # but require at least one option to be selected to proceed.
        if not (use_upper or use_lower or use_digits or use_symbols):
            raise forms.ValidationError(
                "You must select at least one character type to generate a password!"
            )

        return cleaned_data



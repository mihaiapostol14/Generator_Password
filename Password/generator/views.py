import secrets
import string

from django.contrib import messages
from django.contrib.auth.password_validation import password_changed
from django.http import HttpResponse
from django.views.generic.edit import FormView


from .forms import (
    GeneratorForm,
    ExportFormatForm
)

from .utils import GeneratorMixin


class PasswordGeneratorView(FormView,GeneratorMixin):
    template_name = 'generator/generator.html'
    form_class = GeneratorForm

    generated_password = None


    def form_valid(self, form):
        data = form.cleaned_data
        length = data.get('length', 12)
        use_uppercase = data.get('uppercase')
        use_lowercase = data.get('lowercase')
        use_numbers = data.get('numbers')
        use_symbols = data.get('symbols')

        char_pool = ''   # string.ascii_letters

        if use_uppercase:
            char_pool += string.ascii_uppercase

        if use_lowercase:
            char_pool += string.ascii_lowercase

        if use_numbers:
            char_pool += string.digits

        if use_symbols:
            char_pool += string.punctuation

        self.generated_password = ''.join(secrets.choice(char_pool) for _ in range(length))
        self.request.session['generated_password'] = self.generated_password # session variable

        return self.render_to_response(
            self.get_context_data()
        )

    def form_invalid(self, form):
        # Django already handles rendering the form with errors
        messages.error(request=self.request, message='Please select at least one character type.')
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context=context, title='Generator Password', password=self.generated_password)

# This view for export password

# class ExportFormatFormView(FormView,GeneratorMixin):
#     form_class = ExportFormatForm
#     template_name = 'generator/export_form.html'
#
#     def form_valid(self, form):
#         file_format = form.cleaned_data.get('file_format')
#         password = self.request.session.get('generated_password', '')
#
#         response = HttpResponse(content=password, content_type=f'plain/{file_format}')
#         response['Content-Disposition'] = f'attachment; filename="yours_password.{file_format}"'
#         return response
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return self.get_mixin_context(context=context, title='Generator Password')

from random import randint

from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from .password_chars import chars
from .utils import GeneratorMixin
from .forms import (
    GeneratorForm,
    ExportFormatForm
)


class GeneratorFormView(FormView, GeneratorMixin):
    form_class = GeneratorForm
    template_name = 'main/home.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.is_valid()
        """Handles form submission and generates a password."""
        count_symbol = form.cleaned_data['count_symbol']
        password = ''.join(chars[randint(0, len(chars) - 1)] for _ in range(count_symbol))  # Generate password

        # Store the password in session so it can be accessed in get_initial
        request.session['generated_password'] = password

        return self.form_valid(self.get_form())  # Process form as valid

    def get_initial(self):
        """Prepopulate form fields with session data."""
        initial = super().get_initial()
        initial['show_password'] = self.request.session.get('generated_password', '')  # Set initial password
        return initial

    def get_success_url(self):
        messages.success(request=self.request, message='Password Successful Generated')
        return reverse_lazy('generator')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context=context,title='Generator Password')


class ExportFormatFormView(FormView, GeneratorMixin):
    form_class = ExportFormatForm
    template_name = 'main/export_form.html'

    def post(self, request, *args, **kwargs):
        show_password = self.request.session.get('generated_password', '')

        response = HttpResponse(content=show_password, content_type='plain/text')
        response['Content-Disposition'] = 'attachment; filename="yours_password.txt"'
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context=context,title='Generator Password')
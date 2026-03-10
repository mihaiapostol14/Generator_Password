from django.urls import path
from . import views

app_name = 'generator'

urlpatterns = [
    path('', views.PasswordGeneratorView.as_view(), name='generator'),
    # path('export/', views.ExportFormatFormView.as_view(), name='export'),
]
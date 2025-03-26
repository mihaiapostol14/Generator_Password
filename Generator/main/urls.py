from django.urls import path
from . import views

urlpatterns = [
    path('', views.GeneratorFormView.as_view(), name='generator'),
    path('export', views.ExportFormatFormView.as_view(), name='export'),

]

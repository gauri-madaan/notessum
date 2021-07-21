from django.urls import path
from .views import formview, pdfview

urlpatterns = [
    path('', formview, name="formview"),
    path('pdf/', pdfview, name="pdfview"),
]

from django.urls import path
from .views import orders, google_picker_view

urlpatterns = [
    path('', orders, name='orders-home'),  # /orders/
    path('file-picker/', google_picker_view, name='file_picker'),  # /orders/file-picker/
]

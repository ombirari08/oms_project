from django.shortcuts import render
from django.conf import settings

def orders(request):
    return render(request, "orders/home.html")

def google_picker_view(request):
    return render(request, 'orders/file_picker.html', {
        'GOOGLE_CLIENT_ID': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
        'GOOGLE_API_KEY': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
    })

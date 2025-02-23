from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from orders.views import google_picker_view  # Import the view
def home(request):
    return HttpResponse("Welcome to OMS!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orders.urls')),
    path('auth/', include('social_django.urls', namespace='social')),

]





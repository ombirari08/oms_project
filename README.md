**Order Management System (OMS) - Documentation**

**Overview**

This project integrates multiple APIs into an Order Management System (OMS) using Django as the backend framework. The key components include:

Google OAuth 2.0 API for user authentication.

Google Picker API for file uploads (e.g., invoices) and reading data in JSON format.

Stripe Webhooks for handling payment status updates.

Task Management System API for efficient order-related task handling.

**Setup Requirements**

Prerequisites

Python 3.8+

Django 4.x

MySQL or PostgreSQL database

Google Cloud account (for OAuth and Picker API setup)

Stripe account (for webhook handling)

**Installation Steps**

**1 )Clone the repository**
git clone https://github.com/your-repo/oms_project.git
cd oms_project

Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

Install dependencies
pip install -r requirements.txt

**Set up environment variables Create a .env file and add:**
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
STRIPE_SECRET_KEY=your_stripe_secret_key
DATABASE_URL=your_database_url
**Apply database migrations**
python manage.py makemigrations
python manage.py migrate
**Run the development server**
python manage.py runserver

Component Implementation

1. Google OAuth 2.0 API Integration

Objective:

Authenticate users within the OMS using Google OAuth 2.0.

**Steps:**
Register your application in Google Cloud Console.
Obtain your client_id and client_secret.
Configure Django Social Authentication:
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
**Add Google authentication URLs:**
from django.urls import path, include
urlpatterns = [
    path('auth/', include('social_django.urls', namespace='social')),
]

**Order Management System (OMS) - Documentation**

**Overview**
- This project integrates multiple APIs into an Order Management System (OMS) using Django as the backend framework. The key components include:
- Google OAuth 2.0 API for user authentication.
- Google Picker API for file uploads (e.g., invoices) and reading data in JSON format.
- Stripe Webhooks for handling payment status updates.
- Task Management System API for efficient order-related task handling.

**Setup Requirements**
- Prerequisites
- Python 3.8+
- Django 4.x
- MySQL or PostgreSQL database
- Google Cloud account (for OAuth and Picker API setup)
- Stripe account (for webhook handling)

### Installation Steps

**Clone the repository**
git clone https://github.com/your-repo/oms_project.git
cd oms_project

**Create and activate a virtual environment**
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

### Install dependencies
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

### Component Implementation

**1. Google OAuth 2.0 API Integration**

****Objective:**
Authenticate users within the OMS using Google OAuth 2.0.
**
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

**2. Google Picker API Integration**
**Objective:**
Enable file uploads through Google Picker and extract data in JSON format.
**Steps:**
**1.Enable Google Drive API in Google Cloud Console.**

**2.Integrate Google Picker in Frontend (HTML/JavaScript):**
### Task Management System API Integration

### Objective
Integrate a task management system for handling order-related tasks.
API Endpoints:
- Get Order Details: /api/orders/<order_id>/
- Get Customer Details: /api/customers/<customer_id>/
- Add Task for an Order: /api/orders/<order_id>/tasks/
- Get All Tasks for an Order: /api/orders/<order_id>/tasks/all/
- Update Task Status: /api/tasks/<task_id>/update/
  
### Installation Guide
```bash
### Installation Guide
git clone https://github.com/your-repo/oms_project.git
cd oms_project
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Example Django View:

### Integrate Google Picker in Frontend (HTML/JavaScript):
<button onclick="loadPicker()">Pick a File</button>
<script src="https://apis.google.com/js/api.js"></script>
### Implement Picker Logic in JavaScript:

<script>
        let developerKey = "{{ GOOGLE_API_KEY }}";
        let clientId = "{{ GOOGLE_CLIENT_ID }}";
        let appId = "omsproject-451808";
        let oauthToken;

        function onApiLoad() {
            gapi.load('auth2', function() {
                gapi.auth2.init({ client_id: clientId });
            });
            gapi.load('picker', onPickerApiLoad);
        }

        function onPickerApiLoad() {
            oauthToken = gapi.auth2.getAuthInstance().currentUser.get().getAuthResponse().access_token;
        }

        function loadPicker() {
            if (!oauthToken) {
                gapi.auth2.getAuthInstance().signIn().then(function(user) {
                    oauthToken = user.getAuthResponse().access_token;
                    createPicker();
                });
            } else {
                createPicker();
            }
        }

        function createPicker() {
            let picker = new google.picker.PickerBuilder()
                .addView(google.picker.ViewId.DOCS)
                .setOAuthToken(oauthToken)
                .setDeveloperKey(developerKey)
                .setCallback(pickerCallback)
                .build();
            picker.setVisible(true);
        }

        function pickerCallback(data) {
            if (data.action === google.picker.Action.PICKED) {
                let file = data.docs[0];
                document.getElementById("file-info").innerHTML = `Selected File: <br> <strong>${file.name}</strong>`;
                console.log('Picked file details:', file);
            }
        }

        onApiLoad();
    </script>

from django.urls import path, include
from . import views

# Add this in order to use it in templates later
app_name = "accounts"

urlpatterns = [

    # This will include the following URL patterns:

    # accounts/login/ [name='login']
    # accounts/logout/ [name='logout']
    # accounts/password_change/ [name='password_change']
    # accounts/password_change/done/ [name='password_change_done']
    # accounts/password_reset/ [name='password_reset']
    # accounts/password_reset/done/ [name='password_reset_done']
    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']
    
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
    
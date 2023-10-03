from django.contrib import admin
from django.urls import path, include
from hello.views import CustomLoginView  # Import your custom login view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', CustomLoginView.as_view(),
         name='login'),  # Use your custom login view
    path('', include('hello.urls')),  # Include your app's URLs
]

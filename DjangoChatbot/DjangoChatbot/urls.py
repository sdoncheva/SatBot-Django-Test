"""
URL configuration for DjangoChatbot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# DjangoChatbot/urls.py

from django.contrib import admin
from django.urls import path, include
from chat.views import login_view
from chat.views import redirect_to_chat  # Imports the redirect view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='root'),
    path('chat/', include(('chat.urls', 'chat'))),  # Includes chat URLs with namespace
    path('login/', login_view, name='login'),
]




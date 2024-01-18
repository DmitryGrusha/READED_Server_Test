"""server_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static

from registration.views import registration_request
from user.views import get_user
from user.views import register_user

from elevenlabs.views import audio_request

urlpatterns = [
    path('admin/', admin.site.urls),

    # registration
    path('registration/', registration_request, name='registration'),

    # user
    path('getUser', get_user),
    path('registerUser', register_user),

    # elevenlabs audio
    path('getAudio', audio_request, name='getAudio')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

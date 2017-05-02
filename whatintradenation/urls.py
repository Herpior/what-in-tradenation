"""whatintradenation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from login import views as login_views

auth_patterns = [
    url(r'^login/$', login_views.log_in, name='login'),
    url(r'^logout/$', login_views.log_out, name='logout'),
    url(r'^register/$', login_views.register, name='register'),
    # url(r'^auth/', include('social.apps.django_app.urls', namespace='oauth')),
]

player_patterns = [
    url(r'^login/$', login_views.log_out, name='account'),
    # url(r'^account/$', player_views.account, name='account'),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include(auth_patterns)),
    url(r'^user/', include(player_patterns)),
    url(r'^', RedirectView.as_view(pattern_name='login', permanent=False)),
]

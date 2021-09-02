from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', lambda r: HttpResponseRedirect('surveyapp/intro')),
    path('surveyapp/', include('surveyapp.urls')),
]

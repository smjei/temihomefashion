from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name='temihomefashion-index'),
    path('sam404', views.sam404, name='temihomefashion-e404'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello, name="hello"),
    path('healthz/', views.healthz_check, name="healthz"),
]

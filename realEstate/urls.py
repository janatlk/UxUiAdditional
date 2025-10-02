
from django.contrib import admin
from django.urls import path
from real_estate import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='main_page'),
]

from django.contrib import admin
from django.urls import path
from real_estate import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.splash_page, name='splash_page'),
    path('companies/',views.companies_page, name='companies_page'),
    path('favorites/',views.favorites_page,name='favorites_page'),
    path('main/',views.main_page,name='main_page'),
    path('settings/',views.settings_page,name='settings_page'),
    path('property/<int:property_id>/', views.render_each_one, name='one_property')
]
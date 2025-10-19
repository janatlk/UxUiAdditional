
from django.contrib import admin
from django.urls import path
from real_estate import views

urlpatterns = [
    path('set-language/<str:lang>/', views.set_language, name='set_language'),
    path('admin/', admin.site.urls, name='admin'),
    path('', views.splash_page, name='splash_page'),
    path('companies/',views.companies_page, name='companies_page'),
    path('companies/<int:company_id>',views.render_each_one_company, name='companies_page_one'),
    path('favorites/',views.favorites_page,name='favorites_page'),
    path('main/',views.main_page,name='main_page'),
    path('settings/',views.settings_page,name='settings_page'),
    path('property/<int:property_id>/', views.render_each_one, name='one_property'),
    path('search/', views.search_view, name='search_page'), 
]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
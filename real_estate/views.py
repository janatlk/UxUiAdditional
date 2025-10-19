from django.shortcuts import render, get_object_or_404
from .models import Property, Companies
from django.db.models import Q

def splash_page(request):
    return render(request, 'SplashScreen.html')
from django.shortcuts import render
from .models import Property, Companies

def main_page(request):
    # Получаем фильтры из GET-запроса
    company_id = request.GET.get('company', '')
    location = request.GET.get('location', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')

    properties = Property.objects.all()

    if company_id:
        properties = properties.filter(company_linked_id=company_id)
    if location:
        properties = properties.filter(location=location)
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)

    # Получаем все компании и уникальные локации для выпадающих списков
    companies = Companies.objects.all()
    locations = Property.objects.values_list('location', flat=True).distinct()

    context = {
        'properties': properties,
        'companies': companies,
        'locations': locations,
        'filters': {
            'company': company_id,
            'location': location,
            'min_price': min_price,
            'max_price': max_price,
        }
    }

    return render(request, 'Main_page.html', context)





def settings_page(request):
    return render(request, 'Settings.html')
def companies_page(request):
    query = request.GET.get('q', '')
    companies = Companies.objects.all()
    context = {
        'companies': companies
    }
    return render(request,'Companies.html',context)
def favorites_page(request):
    favorites_ids = request.session.get('favorites', [])
    
    properties = Property.objects.filter(id__in=favorites_ids)

    return render(request, 'Favorites.html', {'properties': properties})

def render_each_one(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    return render(request,'one_property.html', {'property':property})

def render_each_one_company(request, company_id):
    companies = get_object_or_404(Companies, id=company_id)
    return render(request,'one_company.html', {'companies':companies})

def search_view(request):
    query = request.GET.get('q','') 
    results = []
    if query:
        results = Property.objects.filter(Q(title__icontains=query))
        
    context = {
        'query':query,
        'results':results
    }
    return render(request,'search_results.html',context)
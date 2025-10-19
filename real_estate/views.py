from django.shortcuts import render, get_object_or_404, redirect
from .models import Property, Companies
from django.db.models import Q

# --- Вспомогательная функция ---
def get_template_for_lang(request, template_name):
    lang = request.session.get('lang', 'en')
    return f"{lang}/{template_name}"  # например "en/Main_page.html"

# --- Страницы ---
def splash_page(request):
    return render(request, get_template_for_lang(request, 'SplashScreen.html'))

def main_page(request):
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
    return render(request, get_template_for_lang(request, 'Main_page.html'), context)

def settings_page(request):
    return render(request, get_template_for_lang(request, 'Settings.html'))

def companies_page(request):
    companies = Companies.objects.all()
    context = {'companies': companies}
    return render(request, get_template_for_lang(request, 'Companies.html'), context)

def favorites_page(request):
    favorites_ids = request.session.get('favorites', [])
    properties = Property.objects.filter(id__in=favorites_ids)
    return render(request, get_template_for_lang(request, 'Favorites.html'), {'properties': properties})

def render_each_one(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    return render(request, get_template_for_lang(request, 'one_property.html'), {'property': property})

def render_each_one_company(request, company_id):
    company = get_object_or_404(Companies, id=company_id)
    properties = Property.objects.filter(company_linked=company)
    context = {'company': company, 'properties': properties}
    return render(request, get_template_for_lang(request, 'one_company.html'), context)

def search_view(request):
    query = request.GET.get('q','')
    results = []
    if query:
        results = Property.objects.filter(Q(title__icontains=query))
    context = {'query': query, 'results': results}
    return render(request, get_template_for_lang(request, 'search_results.html'), context)

# --- Смена языка ---
def set_language(request, lang):
    if lang in ['en', 'ru', 'ky']:
        request.session['lang'] = lang
    return redirect(request.META.get('HTTP_REFERER', '/'))

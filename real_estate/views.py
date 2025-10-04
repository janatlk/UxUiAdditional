from django.shortcuts import render, get_object_or_404
from .models import Property
from django.db.models import Q

def splash_page(request):
    return render(request, 'SplashScreen.html')
def main_page(request):
    #фильттр
    query = request.GET.get('q', '')
    location = request.GET.get('location', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    properties = Property.objects.all()
    if query:
        properties = properties.filter(title__icontains=query)
    if location:
        properties = properties.filter(location__icontains=location)
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)

    context = { 
        'properties': properties,
        'filters': {
            'q': query,
            'location': location,
            'min_price': min_price,
            'max_price': max_price,
        }
    }
    
    return render(request, 'Main_page.html', context)





def settings_page(request):
    return render(request, 'Settings.html')
def companies_page(request):
    return render(request,'Companies.html')
def favorites_page(request):
    return render(request,'Favorites.html')
def render_each_one(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    return render(request,'one_property.html', {'property':property})
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
from django.shortcuts import render, get_object_or_404
from .models import Property
from django.db.models import Q

def splash_page(request):
    return render(request, 'SplashScreen.html')
def main_page(request):
    properties = Property.objects.all()
    return render(request, 'Main_page.html', {'properties': properties})
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
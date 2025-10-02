from django.shortcuts import render


def splash_page(request):
    return render(request, 'SplashScreen.html')
def main_page(request):
    return render(request, 'Main_page.html')
def settings_page(request):
    return render(request, 'Settings.html')
def companies_page(request):
    return render(request,'Companies.html')
def favorites_page(request):
    return render(request,'Favorites.html')
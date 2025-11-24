from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def base(request):
    return render(request, 'catalog/base.html')


def catalog(request):
    return render(request, 'catalog/home.html')


def product(request):
    return render(request, 'catalog/product.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html')

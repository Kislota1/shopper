from django.shortcuts import render


def catalog(request):
    return render(request, 'catalog/catalog.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def info(request):
    print('Request method:', request.method)  # Должен выводить POST, если форма отправлена
    if request.method == 'POST':
        print("POST Data:", request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Name: {name}, Email: {email}, Message: {message}')
    return render(request, 'catalog/contacts.html')



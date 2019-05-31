from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    return render(request, 'home.html')

def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()
    return render(request, 'github.html', {'user': user})
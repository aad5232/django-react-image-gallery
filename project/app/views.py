from django.shortcuts import render
import requests
from django.http import JsonResponse

def photo(request):
    url = 'https://pixabay.com/api/?key=42669198-a343f1b75ad83ce5cd7e5c1b3&q=${dogs}&image_type=photo&pretty=true'
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)

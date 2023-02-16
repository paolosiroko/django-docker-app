from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.shortcuts import render
from .models import BitcoinPrice
# Create your views here.

def index(request):
    return render(request,"bitcoinapp/index.html")


def bitcoin_price(request):
    response = requests.get('https://suitecrmdemo.dtbc.eu/service/v4/rest.php')
    print(response)
    json_data = json.dumps(response)
    price = json_data['bpi']['USD']['rate_float']
    bitcoin_price = BitcoinPrice(price=price)
    bitcoin_price.save()
    return render(request, 'bitcoinapp/bitcoin_price.html', {'price': price})


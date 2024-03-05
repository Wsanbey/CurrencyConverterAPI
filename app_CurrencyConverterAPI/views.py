from django.shortcuts import render 
from django.http import JsonResponse

import requests

def home(request):
    return render(request, 'home.html')
 
def convert(request): 

    # Recebendo os parâmetros da solicitação
    from_currency = request.GET.get('from')
    to_currency = request.GET.get('to')
    amount = float(request.GET.get('amount'))

    # Conferir e retornar valores 
    current_rate = get_quotation(from_currency, to_currency)
 
    # Lógica para a conversão monetária  
    converted_amount = amount * current_rate   

    # Retornar os resultados em formato JSON usando JsonResponse
    return JsonResponse({
        'from_currency': from_currency,
        'to_currency': to_currency,
        'original_rate': current_rate,
        'original_amount': amount,
        'converted_amount': converted_amount
    })
 
def get_quotation(from_currency, to_currency ):

    cod_currency = from_currency + to_currency
    
    # URL da API
    url = f"https://economia.awesomeapi.com.br/json/last/{from_currency}-{to_currency}"
 
    try:
        # Fazendo uma solicitação GET para a API e convertendo a resposta para JSON
        response = requests.get(url)
        data = response.json()

        # Acessando o valor do campo 'bid' dentro do objeto 'BRLUSD'
        bid_value = data[cod_currency]['bid'] 
        return float(bid_value)

    except requests.exceptions.RequestException as e:
        print("Erro na solicitação:", e)


from django.shortcuts import render 
from django.http import JsonResponse

def home(request):
 
    return render(request, 'home.html')

     
def convert(request):
    # Recebendo os parâmetros da solicitação
    from_currency = request.GET.get('from')
    to_currency = request.GET.get('to')
    amount = float(request.GET.get('amount'))

    # Lógica para a conversão monetária
    # Por enquanto, vamos apenas retornar uma resposta de exemplo
    # Simular uma conversão de 1 unidade da moeda de origem para a moeda de destino
    converted_amount = amount * 1.5  # Supondo uma taxa de conversão fixa de 1.5

    # Retornar os resultados em formato JSON usando JsonResponse
    return JsonResponse({
        'from_currency': from_currency,
        'to_currency': to_currency,
        'original_amount': amount,
        'converted_amount': converted_amount
    })

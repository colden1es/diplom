from django.shortcuts import render, redirect
from cloudipsp import Api, Checkout
from .models import Item
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def item_buy(request, id):
    item = Item.objects.get(id=id)
    api = Api(merchant_id=1396424, secret_key='test')
    checkout = Checkout(api=api)

    if request.method == 'POST':
        data = {
            "currency": "RUB",
            "amount": str(item.price) + "00"
        }
        url = checkout.url(data).get('checkout_url')
        return redirect(url)

    context = {'item': item}
    return render(request, 'buy.html', context)


@csrf_exempt
def payment_received(request):
    if request.method == 'POST':
        data = request.POST.dict()
        api = Api(merchant_id=1396424, secret_key='test')
        response = api.call('POST', '/transaction/verify', data)
        if response.get('order_status') == 'approved':
            # Обработка успешного платежа
            return HttpResponse('OK')
    return HttpResponse('Error')
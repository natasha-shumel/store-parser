from django.shortcuts import render
from selections.models import Selections
from goods.models import Goods
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta


from django.shortcuts import render, redirect


def index(request):
    data = {}
    data['selections'] = Selections.objects.all()
    return render(request, 'selections/index.html', data)


def view_selection(request, selection_id):
    data = {}
    data['goods'] = Goods.objects.filter(selection_id=selection_id).values()
    return render(request, 'selections/view.html', data)


def parse(request):
    base_url = 'https://www.21vek.by/mobile/all/apple/'
    page_number = 1
    res = []
    tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(tz)
    new_selection = Selections(datetime=datetime.now() + timedelta(hours=3),
                               quantity=0)
    new_selection.save()
    quantity = 0

    while page_number < 6:
        url = base_url + f'page:{page_number}/'
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            products = soup.find_all('li', {'class': 'result__item'})
            if not products:
                break
            for product in products:
                price = 'Нет в наличии'
                name = product.find('span', {'class': 'result__name'}).text.strip()
                span_element = product.find('span', {'class': 'g-item-data'})
                if span_element:
                    price = round(float(span_element.get('data-price')))
                res.append((name, price))
                new_good = Goods(selection_id=Selections(new_selection.id),
                                 name=name,
                                 price=price)
                new_good.save()
                quantity += 1
            page_number += 1
            new_selection.quantity = quantity
            new_selection.save()
        else:
            break

    return redirect('selections')

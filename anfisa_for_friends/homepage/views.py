from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    # Запишите в переменную ice_cream_list новый QuerySet
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description').filter(
            Q(is_published=True) & Q(
                Q(is_on_main=True) | Q(title__contains='пломбир')))
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)

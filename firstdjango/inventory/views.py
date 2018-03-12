# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from inventory.models import Item


def index(request):
    items = Item.objects.exclude(amount=0)
    context = {
        'items': items,
    }
    return render(request, 'inventory/index.html', context)


def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
        # Set the context for the view
        context = {
            'item': item,
        }
    except Item.DoesNotExist:
        raise Http404('This item does not exist')

    return render(request, 'inventory/item_detail.html', context)


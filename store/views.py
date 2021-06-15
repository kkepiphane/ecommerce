from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
# Create your views here.


def store(request):
    if request.user.is_authenticated:
        utilisateur = request.user.utilisateur
        order, created = Order.objects.get_or_create(
            utilisateur=utilisateur, complete=False)
        items = order.element_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0}
        cartItems = order['get_cart_item']

    products = Produit.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):

    if request.user.is_authenticated:
        utilisateur = request.user.utilisateur
        order, created = Order.objects.get_or_create(
            utilisateur=utilisateur, complete=False)
        items = order.element_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0}
        cartItems = order['get_cart_item']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        utilisateur = request.user.utilisateur
        order, created = Order.objects.get_or_create(
            utilisateur=utilisateur, complete=False)
        items = order.element_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0}
        cartItems = order['get_cart_item']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('produitId:', productId)

    utilisateur = request.user.utilisateur
    produit = Produit.objects.get(id=productId)

    order, created = Order.objects.get_or_create(
        utilisateur=utilisateur, complete=False)

    element, created = Element.objects.get_or_create(
        order=order, produit=produit)

    # Condition pour augmenter ou diminiuer les produits dans le panier

    if action == 'add':
        element.quantite = (element.quantite + 1)
    elif action == 'remove':
        element.quantite = (element.quantite - 1)

    element.save()

    if element.quantite <= 0:
        element.delete()

    return JsonResponse('Element est ajoute', safe=False)

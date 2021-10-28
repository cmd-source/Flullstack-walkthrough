from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JpTpqEbcwR16LJZgRtIq6j8bHXqnugCYa9ApNGp8E6DX6NojGmdBqVsK4ygGWC87rKm1DjfjvhUCc3pJY2E4Apw007jw6pstD',
        'stripe_secret_key': 'stripe_secret_key'
    }

    return render(request, template, context)

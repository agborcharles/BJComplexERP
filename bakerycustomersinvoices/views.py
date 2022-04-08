from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, View
from django.urls import reverse_lazy

from django.core.paginator import Paginator

from django.db.models import Sum
from django.db.models import Q

from django.core.paginator import Paginator

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from . models import *
from . forms import *
# Create your views here.

def customers_view(request):
    customers = Customer.objects.all()

    template_name = 'bakerycustomersinvoices/customers.html'
    context = {'customers':customers}
    return render(request, template_name, context)


def customer_details(request, slug):
    customers = Customer.objects.get(slug=slug)
    opening_balance = customers.customeropeningbalance_set.all()
    invoice = customers.invoice_set.all()
    #items = customers.invoiceitem_set.all()


    # Grab the Total Opening balance for the Customer
    opening_balance = list(opening_balance.aggregate(Sum('amount')).values())[0]
    invoice_total = list(invoice.aggregate(Sum('amount')).values())[0]
    discount_total = list(invoice.aggregate(Sum('discount_amount')).values())[0]
    returns = list(invoice.aggregate(Sum('returns')).values())[0]



    # Name of Vendors for Purchase details
    #vendors = purchase.vendor_set.all()

    template_name = 'bakerycustomersinvoices/customer_account.html'
    context = {'customers':customers,
                'opening_balance':opening_balance,
                'invoice_total':invoice_total,
                'discount_total':discount_total,
                'returns':returns,

                }

    return render(request, template_name, context)

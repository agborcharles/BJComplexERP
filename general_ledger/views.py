from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, View
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator

from django.db.models import Sum
from django.db.models import Q, F, When, Case
from django.db.models import Count

from django.core.paginator import Paginator
from django.contrib.auth.models import User
import datetime

from django.http import HttpResponse, JsonResponse
import csv
import xlwt
import pandas as pd
import io


from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from . models import *

# Create your views here.
#----------------------------- Bakery Sales View ----------------------#
def general_ledger_view(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    transactions = GeneralLedger.objects.all()


    #if start_date and end_date:
        #customer =  list(GeneralLedger.objects.filter(created_at__range=[start_date, end_date]).aggregate(total=Count('invoice_id')).values())[0]
        #total_bakerysales = list(bakerysales.filter(created_at__range=[start_date, end_date]).aggregate(Sum('total_amount')).values())[0]
        #bakerysales = bakerysales.filter(created_at__range=[start_date, end_date])
        #boulangerie_sales = list(bakerysales.filter(sub_department__exact='Boulangerie').aggregate(Sum('total_amount')).values())[0]
        #patisserie_sales = list(bakerysales.filter(sub_department__exact='Patisserie').aggregate(Sum('total_amount')).values())[0]

    #else:
        #customer =  list(GeneralLedger.objects.aggregate(total=Count('invoice_id')).values())[0]
        #total_bakerysales = list(bakerysales.aggregate(Sum('total_amount')).values())[0]
        #bakerysales = bakerysales
        #boulangerie_sales = list(bakerysales.filter(sub_department__exact='Boulangerie').aggregate(Sum('total_amount')).values())[0]
        #patisserie_sales = list(bakerysales.filter(sub_department__exact='Patisserie').aggregate(Sum('total_amount')).values())[0]


    template_name = 'general_ledger/general_ledger.html'
    context = { 'transactions':transactions,


                }
    return render(request, template_name, context)
#----------------------------- Bakery Sales View Ends----------------------#

def transaction_details(request, slug):
    trans = get_object_or_404(GeneralLedger, slug=slug)
    #products = Product.objects.all()

    template_name = 'general_ledger/transaction_details.html'
    context = {'trans':trans}
    return render(request, template_name, context)

#----------------------------- Bakery Add SalesView  and Edit View ----------------------#
class add_general_ledger_trans(SuccessMessageMixin, CreateView):
    model = GeneralLedger
    template_name = 'general_ledger/forms/add_gl_transaction.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('general_ledger:general-ledger')
    success_message = 'Transaction Successfully Added !!!'

class edit_general_ledger_trans(SuccessMessageMixin, UpdateView):
    model = GeneralLedger
    template_name = 'general_ledger/forms/edit_gl_transaction.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('general_ledger:general-ledger')
    success_message = 'Transaction Successfully Edited !!!'

#----------------------------- Bakery Add SalesView  and Edit View Ends----------------------#

#

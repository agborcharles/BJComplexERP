from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, View
from django.urls import reverse_lazy

from django.db.models import Sum
from django.db.models import Q

from django.core.paginator import Paginator

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from . models import *
#from . forms import *

from django.http import HttpResponse, JsonResponse
import csv
import xlwt
import pandas as pd
import io

# Create your views here.
def purchase_details(request, slug):
    purchase = Purchase.objects.get(slug=slug)

    # Name of Vendors for Purchase details
    #vendors = purchase.vendor_set.all()

    template_name = 'purchase/invoice-template.html'
    context = {'purchase':purchase}

    return render(request, template_name, context)


def vendors_view(request):
    vendors = Vendor.objects.all()
    #customers = Customer.objects.all()

    #total_customers = customers.count()
    #total_orders = orders.count()
    #active_customers = customers.filter(is_active=True).count()

    template_name = 'purchase/vendors.html'
    context = {'vendors':vendors,
                }
    return render(request, template_name, context)

def vendor_details(request, slug):
    vendor = Vendor.objects.get(slug=slug)

    # DateTime Filter
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    opening_balance = vendor.openingbalance_set.all()
    opening_balance = list(opening_balance.aggregate(Sum('amount')).values())[0]

    purchase = vendor.purchase_set.all()
    #payments = vendor.payment_set.all()
    #account_payables = vendor.purchase_set.filter(Q(account_cr=2))
    #opening_returns = vendor.openingreturn_set.all()

    if start_date:
        purchase = purchase.filter(created__range=[start_date, end_date])
        purchase_plus_vat = list(purchase.filter(created__range=[start_date, end_date]).aggregate(Sum('amount')).values())[0] + list(purchase.filter(created__range=[start_date, end_date]).aggregate(Sum('vat_amount')).values())[0]

        #payments = payments.filter(created__range=[start_date, end_date])
        #total_payments_amount = list(payments.filter(created__range=[start_date, end_date]).aggregate(Sum('amount_paid')).values())[0]

        returns = opening_returns,filter(created__range=[start_date, end_date])
        total_returns = list(opening_returns.filter(created__range=[start_date, end_date]).aggregate(Sum('amount_paid')).values())[0]
        #total_payments_amount = list(payments.filter(created__range=[start_date, end_date]).aggregate(Sum('amount')).values())[0]
        #purchase_direct_payment = list(purchase.filter(created__range=[start_date, end_date]).aggregate(Sum('payment_amount')).values())[0]
        #total_account_payables = list(account_payables.filter(created__range=[start_date, end_date]).aggregate(Sum('amount')).values())[0]
        #total_balance_due = list(purchase.filter(created__range=[start_date, end_date]).aggregate(Sum('balance_due')).values())[0]
        #total_opening_returns = list(opening_returns.filter(created__range=[start_date, end_date]).aggregate(Sum('amount')).values())[0]

    else:
        purchase = purchase
        purchase_plus_vat = list(purchase.aggregate(Sum('amount')).values())[0] + list(purchase.aggregate(Sum('vat_amount')).values())[0]

        #payments = payments
        #total_payments_amount = list(payments.aggregate(Sum('amount_paid')).values())[0]

        #returns = opening_returns
        #total_returns = list(opening_returns.aggregate(Sum('amount')).values())[0]

        #purchase_direct_payment = list(purchase.aggregate(Sum('payment_amount')).values())[0]
        #total_account_payables = list(account_payables.aggregate(Sum('amount')).values())[0]
        #total_balance_due = list(purchase.aggregate(Sum('balance_due')).values())[0]
        #total_opening_returns = list(opening_returns.aggregate(Sum('amount')).values())[0]


    #total_purchases = list(Purchase.objects.filter(created__range=[start_date, end_date]).aggregate(Sum('amount')).values())[0]
    #total_purchase_amount = list(purchase.aggregate(Sum('amount')).values())[0]
    #total_payments_amount = list(payments.aggregate(Sum('amount')).values())[0]
    #purchase_direct_payment = list(purchase.aggregate(Sum('payment_amount')).values())[0]
    #purchase_plus_vat = list(purchase.aggregate(Sum('amount')).values())[0] + list(purchase.aggregate(Sum('vat_amount')).values())[0]
    #total_balance_due = list(purchase.aggregate(Sum('balance_due')).values())[0]

    lastest_purchase = vendor.purchase_set.last()

    #account_balance = opening_balance + purchase_plus_vat - purchase_direct_payment - total_opening_returns - total_payments_amount

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')


    template_name = 'purchase/vendor_account.html'

    context = {'vendor':vendor,

                'purchases':purchase,
                'purchase_plus_vat':purchase_plus_vat,

                #'payments':payments,
                #'total_payments_amount':total_payments_amount,

                #'returns':returns,
                #'total_returns':total_returns,
                }

    return render(request, template_name, context)


class add_vendor(SuccessMessageMixin, CreateView):
    model = Vendor
    template_name = 'purchase/forms/add_vendor.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('purchase:vendors')
    success_message = 'Vendor Accounts Successfully Created !!!'

class edit_vendor(SuccessMessageMixin, UpdateView):
    model = Vendor
    template_name = 'purchase/forms/edit_vendor.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('purchase:vendors')
    success_message = 'Vendor Accounts Successfully Edited !!!'


def purchase_invoice_client_view(request):
    purchases = Purchase.objects.all()
    vendors = Vendor.objects.all()

    #total_customers = customers.count()
    #total_orders = orders.count()
    #active_customers = customers.filter(is_active=True).count()

    template_name = 'purchase/index.html'
    context = {'purchases':purchases, 'vendors':vendors,
                }
    return render(request, template_name, context)


def purchase_invoice_view(request):
    purchases = Purchase.objects.all()

    template_name = 'purchase/invoices.html'
    context = {'purchases':purchases, 'vendors':vendors,
                }
    return render(request, template_name, context)


#class PurchaseDetailView(DetailView):
    #model = Purchase
    #template_name = 'purchase/invoice-template.html'


class add_purchase(SuccessMessageMixin, CreateView):
    model = Purchase
    template_name = 'purchase/forms/add_purchase.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('purchase:invoices')
    success_message = 'Purchase Accounts Successfully Created !!!'

class edit_purchase(SuccessMessageMixin, UpdateView):
    model = Purchase
    template_name = 'purchase/forms/edit_purchase.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('purchase:invoices')
    success_message = 'Purchase Record Successfully Modified!!!'


def invoices_view(request):
    purchases = Purchase.objects.all()
    vendors = Vendor.objects.all()
    #departments = Department.objects.all()

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date:
        purchases = Purchase.objects.filter(Q(created__range=[start_date, end_date]))
        total_purchases = list(Purchase.objects.filter(created__range=[start_date, end_date]).aggregate(Sum('amount')).values())[0]
        total_vat_amount= list(Purchase.objects.filter(created__range=[start_date, end_date]).aggregate(Sum('vat_amount')).values())[0]
        total_purchase_plus_vat = total_purchases + total_vat_amount

    else:
        purchases = Purchase.objects.all()
        total_purchases = list(Purchase.objects.aggregate(Sum('amount')).values())[0]
        total_vat_amount= list(Purchase.objects.aggregate(Sum('vat_amount')).values())[0]

        total_purchase_plus_vat = total_purchases + total_vat_amount

    template_name = 'purchase/invoices.html'
    context = {
                'purchases':purchases,
                }
    return render(request, template_name, context)

def export_purchase_csv(request):
    data = pd.DataFrame(list(Purchase.objects.values()))
    if len(data) > 0:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Purchase Data' + ' ' + \
            str(datetime.datetime.now())+'.csv'
        data.to_csv(path_or_buf = response,sep=',', float_format='%.2f', index=False, decimal=".")

        return response

    return redirect('invoices')

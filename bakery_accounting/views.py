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
def bakerysales_view(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    bakerysales = BakerySales.objects.all()
    customer = list(BakerySales.objects.aggregate(total=Count('invoice_id')).values())[0]
    boulangerie_sales = list(bakerysales.filter(sub_department__exact='Boulangerie').aggregate(Sum('total_amount')).values())[0]
    patisserie_sales = list(bakerysales.filter(sub_department__exact='Patisserie').aggregate(Sum('total_amount')).values())[0]

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        customer =  list(BakerySales.objects.filter(created_at__range=[start_date, end_date]).aggregate(total=Count('invoice_id')).values())[0]
        total_bakerysales = list(bakerysales.filter(created_at__range=[start_date, end_date]).aggregate(Sum('total_amount')).values())[0]
        bakerysales = bakerysales.filter(created_at__range=[start_date, end_date])
        boulangerie_sales = list(bakerysales.filter(sub_department__exact='Boulangerie').aggregate(Sum('total_amount')).values())[0]
        patisserie_sales = list(bakerysales.filter(sub_department__exact='Patisserie').aggregate(Sum('total_amount')).values())[0]

    else:
        customer =  list(BakerySales.objects.aggregate(total=Count('invoice_id')).values())[0]
        total_bakerysales = list(bakerysales.aggregate(Sum('total_amount')).values())[0]
        bakerysales = bakerysales
        boulangerie_sales = list(bakerysales.filter(sub_department__exact='Boulangerie').aggregate(Sum('total_amount')).values())[0]
        patisserie_sales = list(bakerysales.filter(sub_department__exact='Patisserie').aggregate(Sum('total_amount')).values())[0]

    current_user = request.user
    current_user = current_user.id

    template_name = 'bakery_accounting/bakeryproductsales.html'
    context = { 'bakerysales':bakerysales,
                'total_bakerysales':total_bakerysales,
                'customer':customer,
                'boulangerie_sales':boulangerie_sales,
                'patisserie_sales':patisserie_sales,

                #'total_expenditure':total_expenditure,
                'current_user':current_user,

                }
    return render(request, template_name, context)
#----------------------------- Bakery Sales View Ends----------------------#

#----------------------------- Bakery Sales Upload View ----------------------#
def bakery_sales_upload(request):

    template_name = 'bakery_accounting/invoices_upload.html'
    prompt = {'order': 'Order of the CSV Should be date, department, employee, transactionId, institutions \
                    institutions, description, amount account_dr, account_cr'}

    if request.method == "GET":
        return render(request, template_name, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a CSV File')

    dataset = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(dataset)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = BakerySales.objects.update_or_create(
            id= column[0],
            created_at = column[1],
            order_no =column[2],
            invoice_id = column[3],
            supplier = column[4],
            customer = column[5],
            department = column[6],
            sub_department = column[7],
            category = column[8],
            session = column[9],
            product = column[10],
            qty = column[11],
            cost_price = column[12],
            total_amount = column[13],
            discount = column[14],
            discount_value = column[15],
            net_amount = column[16],
            commission = column[17],
        )
            #return redirect('expenses')
    context = {}
    return render(request, template_name, context)

#----------------------------- Bakery Sales Upload View Ends----------------------#

#----------------------------- Bakery Add SalesView  and Edit View ----------------------#
class add_bakery_sales(SuccessMessageMixin, CreateView):
    model = BakerySales
    template_name = 'bakery_accounting/forms/add_bakery_sales.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bakery_accounting:bakerysales')
    success_message = 'Sales Successfully Edited !!!'

class edit_bakery_sales(SuccessMessageMixin, UpdateView):
    model = BakerySales
    template_name = 'bakery_accounting/forms/edit_bakery_sales.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bakery_accounting:bakerysales')
    success_message = 'Sales Successfully Created !!!'

#----------------------------- Bakery Add SalesView  and Edit View Ends----------------------#

#----------------------------- Bakery Payment View----------------------#
def bakery_payments_view(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    bakerypayments = BakeryPayment.objects.all()

    if start_date and end_date:
        total_bakerypayments = list(bakerypayments.filter(created_at__range=[start_date, end_date]).aggregate(Sum('amount')).values())[0]
        bakerypayments = bakerypayments.filter(created_at__range=[start_date, end_date])
    else:
        total_bakerypayments = list(bakerypayments.aggregate(Sum('amount')).values())[0]
        bakerypayments = bakerypayments



    template_name = 'bakery_accounting/payments/bakerypayments.html'
    context = {
                'bakerypayments':bakerypayments,
                'total_bakerypayments':total_bakerypayments,

                }
    return render(request, template_name, context)

#----------------------------- Bakery Payment View Ends----------------------#
#----------------------------- Bakery Sales Upload View ----------------------#
def bakery_payments_upload(request):

    template_name = 'bakery_accounting/payments/payments_upload.html'
    prompt = {'order': 'Order of the CSV Should be date, department, employee, transactionId, institutions \
                    institutions, description, amount account_dr, account_cr'}

    if request.method == "GET":
        return render(request, template_name, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a CSV File')

    dataset = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(dataset)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = BakeryPayment.objects.update_or_create(
            id= column[0],
            created_at = column[1],
            department =column[2],
            session = column[3],
            collector = column[4],
            payment_id = column[5],
            customer = column[6],
            amount = column[7],

        )
            #return redirect('expenses')
    context = {}
    return render(request, template_name, context)

#----------------------------- Bakery Sales Upload View Ends----------------------#
#----------------------------- Bakery Add SalesView  and Edit View ----------------------#
class add_bakery_payments(SuccessMessageMixin, CreateView):
    model = BakeryPayment
    template_name = 'bakery_accounting/payments/forms/add_bakery_payment.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bakery_accounting:bakerypayments')
    success_message = 'Payments Successfully Edited !!!'

class edit_bakery_payments(SuccessMessageMixin, UpdateView):
    model = BakeryPayment
    template_name = 'bakery_accounting/payments/forms/edit_bakery_payment.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bakery_accounting:bakerypayments')
    success_message = 'Payments Successfully Created !!!'

#----------------------------- Bakery Add SalesView  and Edit View Ends----------------------#
#----------------------------- Bakery Payment View----------------------#
def bakery_returns_view(request):
    bakeryreturns = BakeryReturn.objects.all()

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        total_bakeryreturns = list(bakeryreturns.filter(created_at__range=[start_date, end_date]).aggregate(Sum('total_amount')).values())[0]
        bakeryreturns = bakeryreturns.filter(created_at__range=[start_date, end_date])
    else:
        total_bakeryreturns = list(bakeryreturns.aggregate(Sum('total_amount')).values())[0]
        bakeryreturns = bakeryreturns

    template_name = 'bakery_accounting/returns/bakeryreturns.html'
    context = {
                'bakeryreturns':bakeryreturns,
                'total_bakeryreturns':total_bakeryreturns,

                }
    return render(request, template_name, context)

#----------------------------- Bakery Payment View Ends----------------------#
#----------------------------- Bakery Sales Upload View ----------------------#
def bakery_returns_upload(request):

    template_name = 'bakery_accounting/returns/returns_upload.html'
    prompt = {'order': 'Order of the CSV Should be date, department, employee, transactionId, institutions \
                    institutions, description, amount account_dr, account_cr'}

    if request.method == "GET":
        return render(request, template_name, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a CSV File')

    dataset = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(dataset)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = BakeryReturn.objects.update_or_create(
            id= column[0],
            created_at = column[1],
            return_id =column[2],
            invoice_id = column[3],
            customer_from = column[4],
            customer_to = column[5],
            department = column[6],
            sub_department = column[7],
            category = column[8],
            product = column[9],
            qty = column[10],
            cost_price = column[11],
            total_amount = column[12],

        )
            #return redirect('expenses')
    context = {}
    return render(request, template_name, context)

#----------------------------- Bakery Sales Upload View Ends----------------------#
#----------------------------- Bakery Add SalesView  and Edit View ----------------------#
class add_bakery_returns(SuccessMessageMixin, CreateView):
    model = BakeryReturn
    template_name = 'bakery_accounting/returns/forms/add_bakery_returns.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bakery_accounting:bakeryreturns')
    success_message = 'Payments Successfully Edited !!!'

class edit_bakery_returns(SuccessMessageMixin, UpdateView):
    model = BakeryReturn
    template_name = 'bakery_accounting/returns/forms/edit_bakery_returns.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bakery_accounting:bakeryreturns')
    success_message = 'Payments Successfully Created !!!'

#----------------------------- Bakery Add SalesView  and Edit View Ends----------------------#


#----------------------------- Bakery Opening Bal View----------------------#
def bakery_opening_bal_view(request):
    bakery_opening_bal = BakeryOpeningBalances.objects.all()

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        total_bakery_opening_bal = list(bakery_opening_bal.filter(created_at__range=[start_date, end_date]).aggregate(Sum('total_amount')).values())[0]
        bakerypayments = bakery_opening_bal.filter(created_at__range=[start_date, end_date])
    else:
        total_bakery_opening_bal = list(bakery_opening_bal.aggregate(Sum('total_amount')).values())[0]
        bakery_opening_bal = bakery_opening_bal

    template_name = 'bakery_accounting/opening_balance/bakery_opening_bal.html'
    context = {
                'bakery_opening_bal':bakery_opening_bal,
                'total_bakery_opening_bal':total_bakery_opening_bal,

                }
    return render(request, template_name, context)

#----------------------------- Bakery Payment View Ends----------------------#
#----------------------------- Bakery Sales Upload View ----------------------#
def bakery_opening_bal_upload(request):

    template_name = 'bakery_accounting/opening_balance/opening_bal_upload.html'
    prompt = {'order': 'Order of the CSV Should be date, department, employee, transactionId, institutions \
                    institutions, description, amount account_dr, account_cr'}

    if request.method == "GET":
        return render(request, template_name, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a CSV File')

    dataset = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(dataset)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = BakeryOpeningBalances.objects.update_or_create(
            id= column[0],
            created_at = column[1],
            department =column[2],
            openingbalance_id= column[3],
            customer = column[4],
            total_amount = column[5],
        )
            #return redirect('expenses')
    context = {}
    return render(request, template_name, context)

#----------------------------- Bakery Sales Upload View Ends----------------------#
#----------------------------- Bakery Add SalesView  and Edit View ----------------------#
class add_bakery_opening_bal(SuccessMessageMixin, CreateView):
    model = BakeryReturn
    template_name = 'bakery_accounting/opening_balance/forms/add_bakery_opening_bal.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bakery_accounting:bakery-opening-bal')
    success_message = 'Opening Balance Successfully Edited !!!'

class edit_bakery_opening_bal(SuccessMessageMixin, UpdateView):
    model = BakeryReturn
    template_name = 'bakery_accounting/opening_balance/forms/add_bakery_opening_bal.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bakery_accounting:bakery-opening-bal')
    success_message = 'Opening Balance Successfully Created !!!'

#----------------------------- Bakery Add SalesView  and Edit View Ends----------------------#

#----------------------------- Bakery Inventory View ----------------------#
def bakery_inventory_view(request):
    bakery_inventory = BakeryInventoryMagazine.objects.all()

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        total_bakery_inventory = list(bakery_inventory.filter(created_at__range=[start_date, end_date]).aggregate(Sum('total_cost_price')).values())[0]
        bakery_inventory= bakery_inventory.filter(created_at__range=[start_date, end_date])
        opening_stock = list(bakery_inventory.filter(stock_status__exact='Opening Stock').aggregate(Sum('total_cost_price')).values())[0]
        closing_stock = list(bakery_inventory.filter(stock_status__exact='Closing Stock').aggregate(Sum('total_cost_price')).values())[0]

    else:
        total_bakery_inventory = list(bakery_inventory.aggregate(Sum('total_cost_price')).values())[0]
        bakery_inventory = bakery_inventory
        opening_stock = list(bakery_inventory.filter(stock_status__exact='Opening Stock').aggregate(Sum('total_cost_price')).values())[0]
        closing_stock = list(bakery_inventory.filter(stock_status__exact='Closing Stock').aggregate(Sum('total_cost_price')).values())[0]

    template_name = 'bakery_accounting/bakery_inventory/bakery_inventory.html'
    context = { 'bakery_inventory':bakery_inventory,
                'total_bakery_inventory':total_bakery_inventory,
                'opening_stock':opening_stock,
                'closing_stock':closing_stock,

                }
    return render(request, template_name, context)
#----------------------------- Bakery Sales View Ends----------------------#

#----------------------------- Bakery Add SalesView  and Edit View ----------------------#
class add_bakery_inventory(SuccessMessageMixin, CreateView):
    model = BakeryInventoryMagazine
    template_name = 'bakery_accounting/bakery_inventory/forms/add_bakery_inventory.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bakery_accounting:bakery-inventory')
    success_message = 'Inventory Successfully Edited !!!'

class edit_bakery_inventory(SuccessMessageMixin, UpdateView):
    model = BakeryInventoryMagazine
    template_name = 'bakery_accounting/bakery_inventory/forms/edit_bakery_inventory.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bakery_accounting:bakery-inventory')
    success_message = 'Inventory Successfully Created !!!'

#----------------------------- Bakery Add SalesView  and Edit View Ends----------------------#



#----------------------------- Bakery Sales View ----------------------#
def bakery_purchases_view(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    bakerypurchases = BakeryPurchase.objects.all()

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        total_bakery_purchases = list(bakerypurchases.filter(created_at__range=[start_date, end_date]).aggregate(Sum('total_cost_price')).values())[0]
        bakerypurchases = bakerypurchases.filter(created_at__range=[start_date, end_date])

        direct_rm_purchases = bakerypurchases.filter(category__exact='Direct')
        direct_rm_purchases = list(bakerypurchases.filter(created_at__range=[start_date, end_date]).aggregate(Sum('total_cost_price')).values())[0]
        indirect_rm_purchases = list(bakerypurchases.filter(category__exact='Indirect').aggregate(Sum('total_cost_price')).values())[0]

    else:
        bakerypurchases = bakerypurchases
        total_bakery_purchases = list(bakerypurchases.aggregate(Sum('total_cost_price')).values())[0]
        direct_rm_purchases = list(bakerypurchases.filter(category__exact='Direct').aggregate(Sum('total_cost_price')).values())[0]
        indirect_rm_purchases = list(bakerypurchases.filter(category__exact='Indirect').aggregate(Sum('total_cost_price')).values())[0]



    template_name = 'bakery_accounting/bakerypurchases/bakerypurchases.html'
    context = {
                'bakerypurchases':bakerypurchases,
                'total_bakery_purchases':total_bakery_purchases,
                'direct_rm_purchases':direct_rm_purchases,
                'indirect_rm_purchases':indirect_rm_purchases,
                }
    return render(request, template_name, context)
#----------------------------- Bakery Sales View Ends----------------------#

#----------------------------- Bakery Add SalesView  and Edit View ----------------------#
class add_bakery_purchase(SuccessMessageMixin, CreateView):
    model = BakeryPurchase
    template_name = 'bakery_accounting/bakerypurchases/forms/add_bakery_purchase.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bakery_accounting:bakerypurchases')
    success_message = 'Bakery Purchase Successfully !!!'

class edit_bakery_purchase(SuccessMessageMixin, UpdateView):
    model = BakeryPurchase
    template_name = 'bakery_accounting/bakerypurchases/forms/edit_bakery_purchase.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bakery_accounting:bakerypurchases')
    success_message = 'Bakery Purchase Successfully Edited!!!'

#----------------------------- Bakery Add SalesView  and Edit View Ends----------------------#


#----------------------------- Bakery Sales View ----------------------#
def bakery_rm_damages_view(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    bakery_rm_damages = BakeryRmDamages.objects.all()

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        total_bakery_rm_damages = list(bakery_rm_damages.filter(created_at__range=[start_date, end_date]).aggregate(Sum('total_cost_price')).values())[0]
        bakery_rm_damages = bakery_rm_damages.filter(created_at__range=[start_date, end_date])

    else:
        bakery_rm_damages = bakery_rm_damages
        total_bakery_rm_damages = list(bakery_rm_damages.aggregate(Sum('total_cost_price')).values())[0]

    template_name = 'bakery_accounting/bakery_rm_damages/bakery_rm_damages.html'
    context = {
                'bakery_rm_damages':bakery_rm_damages,
                'total_bakery_rm_damages':total_bakery_rm_damages,
                }
    return render(request, template_name, context)
#----------------------------- Bakery Sales View Ends----------------------#

#----------------------------- Bakery Add SalesView  and Edit View ----------------------#
class add_bakery_rm_damages(SuccessMessageMixin, CreateView):
    model = BakeryRmDamages
    template_name = 'bakery_accounting/bakery_rm_damages/forms/add_bakery_rm_damages.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bakery_accounting:bakery-rm-damages')
    success_message = 'Bakery RM Damage Successfully !!!'

class edit_bakery_rm_damages(SuccessMessageMixin, UpdateView):
    model = BakeryRmDamages
    template_name = 'bakery_accounting/bakery_rm_damages/forms/edit_bakery_rm_damages.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bakery_accounting:bakery-rm-damages')
    success_message = 'Bakery RM Damage Successfully Edited!!!'

#----------------------------- Bakery Add SalesView  and Edit View Ends----------------------#

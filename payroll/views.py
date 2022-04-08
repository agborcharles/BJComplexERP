from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, View
from django.urls import reverse_lazy

from django.db.models import Sum
from django.db.models import Q

from django.core.paginator import Paginator

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from . models import *
from . forms import *

from django.http import HttpResponse, JsonResponse
import csv
import xlwt
import pandas as pd
import io

# Create your views here.
def employee_view(request):
    employees = Employee.objects.all()
    #customers = Customer.objects.all()

    #total_customers = customers.count()
    #total_orders = orders.count()
    #active_customers = customers.filter(is_active=True).count()

    template_name = 'payroll/employees.html'
    context = {'employees':employees,
                }
    return render(request, template_name, context)

def employee_details(request, slug):
    employee = Employee.objects.get(slug=slug)

    # DateTime Filter
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    salaries = employee.salaries_set.all()

    template_name = 'payroll/employee-profile.html'
    context = { 'employee':employee,
                'salaries':salaries,

                }

    return render(request, template_name, context)


class add_employee(SuccessMessageMixin, CreateView):
    model = Employee
    template_name = 'payroll/add_employee.html'
    fields = '__all__'
    exclude = ('slug', 'employeeid',)
    success_url = reverse_lazy('payroll:employee')
    success_message = 'Employee Successfully Created !!!'

class edit_employee(SuccessMessageMixin, UpdateView):
    model = Employee
    template_name = 'payroll/edit_employee.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('payroll:employee')
    success_message = 'Employee Successfully Edited !!!'


def salary_view(request):
    salaries = Salaries.objects.all()
    #customers = Customer.objects.all()
    #active_customers = customers.filter(is_active=True).count()

    template_name = 'payroll/salaries.html'
    context = {'salaries':salaries,
                }
    return render(request, template_name, context)

class add_salaries(SuccessMessageMixin, CreateView):
    model = Salaries
    template_name = 'payroll/add_salaries.html'
    fields = '__all__'
    exclude = ('slug', 'employeeid',)
    success_url = reverse_lazy('payroll:salary')
    success_message = 'Salary Successfully Created !!!'

class edit_salaries(SuccessMessageMixin, UpdateView):
    model = Salaries
    template_name = 'payroll/edit_salaries.html'
    fields = '__all__'
    exclude = ('slug', 'employeeid',)
    success_url = reverse_lazy('payroll:salary')
    success_message = 'Salary Successfully Edited !!!'

class salaryDetailView(DetailView):
    model = Salaries
    template_name = 'payroll/pay_slip.html'

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, View
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from . models import *
from configurations.models import *
# Create your views here.

def contacts_home(request):
    contacts = Contact.objects.all().order_by('-created_at')


    search_query = request.GET.get('search',  '')
    #if search_query:
        #tasks =Task.objects.filter(Q(depart__icontains=search_query))
    template_name = 'contact_list/contactlist.html'
    context = {'contacts':contacts}

    return render(request, template_name, context)


def contacts_detail(request, slug):
    contacts = get_object_or_404(Contact, slug=slug)
    #products = Product.objects.all()

    template_name = 'contact_list/contact_details.html'
    context = {'contacts':contacts}
    return render(request, template_name, context)

'''

class add_task(SuccessMessageMixin, CreateView):
    model = Task
    template_name = 'task/forms/add_task.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('task:task-home')
    success_message = 'The Task have been successfully Created'

class edit_task(SuccessMessageMixin, UpdateView):
    model = Task
    template_name = 'task/forms/edit_task.html'
    fields = [ 'employee', 'comments', 'priority', 'state', 'expiry_date']
    exclude = ('slug',)
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('task:task-home')
    success_message = 'The Task have been successfully Edited'
'''

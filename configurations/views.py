from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, View
from django.urls import reverse_lazy
from django.db.models import Q
from . models import *

# Create your views here.
'''
def EmployeesView(request):
    employees = Worker.objects.all().order_by('-created')


    search_query = request.GET.get('search',  '')
    if search_query:
        employees = Worker.objects.filter(Q(first_name__icontains=search_query)
                                        |Q(middle_name__icontains=search_query)
                                        |Q(last_name__icontains=search_query)
                                        )

    template_name = 'configurations/index.html'
    context = {'employees':employees}

    return render(request, template_name, context)


def worker_detail(request, slug):
    employee = get_object_or_404(Worker, slug=slug)
    #products = Product.objects.all()

    template_name = 'configurations/employee_details.html'
    context = {'employee':employee}
    return render(request, template_name, context)
'''
'''
class worker_detail(View):
    def get(self, request, *args, **kwargs):
        worker = get_object_or_404(Worker, pk=kwargs['pk'])
        context = {'worker':worker}
        template_name = 'configurations/employee_details.html'
        return render(request, template_name, context)
'''
'''
class add_department(CreateView):
    model = Department
    template_name = 'configurations/add_department.html'
    fields = '__all__'
    success_url = reverse_lazy('configurations:home')

class add_role(CreateView):
    model = Role
    template_name = 'configurations/add_role.html'
    fields = '__all__'
    success_url = reverse_lazy('configurations:home')

class add_worker(CreateView):
    model = Worker
    template_name = 'configurations/add_worker.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('configurations:home')

class edit_worker(UpdateView):
    model = Worker
    template_name = 'configurations/edit_worker.html'
    fields = '__all__'
    exclude = ('slug',)
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('configurations:home')

class delete_worker(DeleteView):
    model = Worker
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('configurations:home')
    template_name = 'configurations/delete_worker.html'
'''

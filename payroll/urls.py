from django.urls import path
from . import views

app_name = 'payroll'

urlpatterns = [
    path('', views.employee_view, name='employee'),
    path('add-employee/', views.add_employee.as_view(), name='add-employee'),
    path('edit-employee/<int:pk>/', views.edit_employee.as_view(), name='edit-employee'),
    path('employee-detail/<slug:slug>/',views.employee_details, name='employee-detail'),

    path('salary/', views.salary_view, name='salary'),
    path('add-salaries/', views.add_salaries.as_view(), name='add-salaries'),
    path('edit-salaries/<int:pk>/', views.edit_salaries.as_view(), name='edit-salaries'),
    path('salary/<int:pk>', views.salaryDetailView.as_view(), name='salary-details'),
    #path('employee-detail/<slug:slug>/',vieemployee_account_details, name='employee-detail'),
    #path('salary-transactions', views.salary_transactions, name='salary-transactions'),
    #path('purchase-details/<slug:slug>', views.purchase_details, name='purchase-details'),

    #path('add-salary/', views.add_salary.as_view(), name='add-salary'),

]

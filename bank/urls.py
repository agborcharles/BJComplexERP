from django.urls import path
from . import views

app_name = 'bank'

urlpatterns = [
    path('', views.bank_view, name='bank'),
    path('bank-transactions', views.bank_transactions, name='bank-transactions'),
    path('account-detail/<slug:slug>/',views.bank_account_details, name='account-detail'),
    path('add-deposit/', views.add_deposit.as_view(), name='add-deposit'),
    path('add-withdrawal/', views.add_withdrawal.as_view(), name='add-withdrawal'),
    path('account-opening_bal/', views.add_account_opening_bal.as_view(), name='account-opening-bal'),
    path('add-bank-charges/', views.add_bank_charges.as_view(), name='add-bank-charges'),
    path('edit-deposit/<int:pk>/', views.edit_deposit.as_view(), name='edit-deposit'),
    path('edit-withdrawal/<int:pk>/', views.edit_withdrawal.as_view(), name='edit-withdrawal'),
    path('edit-account-opening-bal/<int:pk>/', views.edit_account_opening_bal.as_view(), name='edit-account-opening-bal'),



    #path('worker-detail/<slug:slug>/',views.worker_detail, name='worker-detail'),

    #path('add-department/', views.add_department.as_view(), name='add-department'),
    #path('add-role/', views.add_role.as_view(), name='add-role'),
    #path('edit-worker/<int:pk>/', views.edit_worker.as_view(), name='edit-worker'),
    #path('delete-worker/<int:pk>/', views.delete_worker.as_view(), name='delete-worker'),



]

from django.urls import path
from . import views

app_name = 'bakerycustomersinvoices'

urlpatterns = [
    #path('', views.home, name='home'),

    path('', views.customers_view, name='customers'),
    #path('add-customer/', views.add_customer.as_view(), name='add-customer'),
    #path('edit-customer/<int:pk>/', views.edit_customer.as_view(), name='edit-customer'),
    path('customer-details/<slug:slug>/', views.customer_details, name='customer-details'),

    #path('opening-balance/', views.opening_balance_view, name='opening-balance'),
    #path('add-opening-balance/', views.add_opening_balance, name='add-opening-balance'),
    #path('edit-opening-balance/<int:pk>/', views.edit_opening_balance.as_view(), name='edit-opening-balance'),
    #path('delete-opening-balance/<int:pk>/delete/', views.delete_opening_balance.as_view(), name='delete-opening-balance'),

    #path('departments/', views.departments_view, name='departments'),
    #path('categories/', views.categories_view, name='categories'),
    #path('products/', views.products_view, name='products'),


    #path('invoice/', views.invoice_view, name='invoice'),
    #path('print-details-invoice/<int:invoice_id>/', views.invoice_details_print, name='print-details-invoice'),
    #path('add-order/', views.add_order_view, name='add-order'),
    #path('edit-invoice/<int:pk>/', views.edit_order.as_view(), name='edit-invoice'),

    #path('invoice-payments/', views.InvoicePayment_view, name='invoice-payments'),
    #path('add-payment/', views.add_payment_view.as_view(), name='add-payment'),
    #path('edit-payment/<int:pk>/', views.edit_payment.as_view(), name='edit-payment'),

    #path('damages/', views.damages_view, name='damages'),
    #path('add-damage/', views.add_damage_view.as_view(), name='add-damage'),
    #path('edit-damages/<int:pk>/', views.edit_damages.as_view(), name='edit-damages'),

    #path('returns/', views.returns_view, name='returns'),
    #path('add-return/', views.add_return_view.as_view(), name='add-return'),
    #path('edit-returns/<int:pk>/', views.edit_returns.as_view(), name='edit-returns'),

    #path('commission/', views.commissionearned_view, name='commission'),
    #path('add-commission/', views.add_commission_view.as_view(), name='add-commission'),
    #path('edit-commission/<int:pk>/', views.edit_commission.as_view(), name='edit-commission'),
    #path('add-order/', views.add_order_view, name='add-order'),

]

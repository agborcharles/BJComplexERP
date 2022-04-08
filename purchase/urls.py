from django.urls import path
from . import views

app_name = 'purchase'

urlpatterns = [

    path('', views.purchase_invoice_client_view, name='purchases'),
    path('invoices', views.invoices_view, name='invoices'),
    path('add-purchase/', views.add_purchase.as_view(), name='add-purchase'),
    path('edit-purchase/<int:pk>/', views.edit_purchase.as_view(), name='edit-purchase'),
    #path('purchase-details/<int:pk>', views.PurchaseDetailView.as_view(), name='purchase-details'),
    path('purchase-details/<slug:slug>', views.purchase_details, name='purchase-details'),

    path('export-csv/', views.export_purchase_csv, name='export-csv'),

    path('vendors', views.vendors_view, name='vendors'),
    path('vendor-details/<slug:slug>/', views.vendor_details, name='vendor-details'),
    #path('add-vendor/', views.add_vendor.as_view(), name='add-vendor'),
    #path('edit-vendor/<int:pk>/', views.edit_vendor.as_view(), name='edit-vendor'),
    #path('invoice/<int:pk>', views.invoiceDetailView.as_view(), name='invoice-details'),

    #path('add-purchase/', views.add_purchase.as_view(), name='add-purchase'),
    #path('edit-purchase/<int:pk>/', views.edit_purchase.as_view(), name='edit-purchase'),
    #path('purchase-details/<slug:slug>/', views.purchase_details, name='purchase-details'),

    #path('suppliers/', views.products, name='suppliers'),
    #path('add-supplier/', views.add_supplier.as_view(), name='add-supplier'),
    #path('edit-supplier/<int:pk>/', views.edit_supplier.as_view(), name='edit-supplier'),

    #path('delete-opening-balance/<int:pk>/delete/', views.delete_opening_balance.as_view(), name='delete-opening-balance'),


]

from django.urls import path
from . import views

app_name = 'bakery_accounting'

urlpatterns = [
    path('', views.bakerysales_view, name='bakerysales'),
    path('bakery-sales-upload/', views.bakery_sales_upload, name='bakery-sales-upload'),
    path('add-bakery-sales/', views.add_bakery_sales.as_view(), name='add-bakery-sales'),
    path('edit-bakery-sales/<int:pk>/', views.edit_bakery_sales.as_view(), name='edit-bakery-sales'),

    path('bakerypayments', views.bakery_payments_view, name='bakerypayments'),
    path('bakery-payments-upload/', views.bakery_payments_upload, name='bakery-payments-upload'),
    path('add-bakery-payments/', views.add_bakery_payments.as_view(), name='add-bakery-payments'),
    path('edit-bakery-payments/<int:pk>/', views.edit_bakery_payments.as_view(), name='edit-bakery-payments'),

    path('bakeryreturns', views.bakery_returns_view, name='bakeryreturns'),
    path('bakery-returns-upload/', views.bakery_returns_upload, name='bakery-returns-upload'),
    path('add-bakery-returns/', views.add_bakery_returns.as_view(), name='add-bakery-returns'),
    path('edit-bakery-returns/<int:pk>/', views.edit_bakery_returns.as_view(), name='edit-bakery-returns'),

    path('bakery-opening-bal', views.bakery_opening_bal_view, name='bakery-opening-bal'),
    path('bakery-opening-bal-upload/', views.bakery_opening_bal_upload, name='bakery-opening-bal-upload'),
    path('add-bakery-opening-bal/', views.add_bakery_opening_bal.as_view(), name='add-bakery-opening-bal'),
    #path('edit-bakery-returns/<int:pk>/', views.edit_bakery_returns.as_view(), name='edit-bakery-returns'),

    path('bakery-inventory', views.bakery_inventory_view, name='bakery-inventory'),
    #path('bakery-opening-bal-upload/', views.bakery_opening_bal_upload, name='bakery-opening-bal-upload'),
    path('add-bakery-inventory/', views.add_bakery_inventory.as_view(), name='add-bakery-inventory'),
    path('edit-bakery-inventory/<int:pk>/', views.edit_bakery_inventory.as_view(), name='edit-bakery-inventory'),


    path('bakerypurchases', views.bakery_purchases_view, name='bakerypurchases'),
    path('add-bakery-purchase/', views.add_bakery_purchase.as_view(), name='add-bakery-purchase'),
    path('edit-bakery-purchase/<int:pk>/', views.edit_bakery_purchase.as_view(), name='edit-bakery-purchase'),

    path('bakery-rm-damages', views.bakery_rm_damages_view, name='bakery-rm-damages'),
    path('add-bakery-rm-damage/', views.add_bakery_rm_damages.as_view(), name='add-bakery-rm-damage'),
    path('edit-bakery-rm-damage/<int:pk>/', views.edit_bakery_rm_damages.as_view(), name='edit-bakery-rm-damage'),

]

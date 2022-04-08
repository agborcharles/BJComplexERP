from django.urls import path
from . import views

app_name = 'general_ledger'

urlpatterns = [
    path('', views.general_ledger_view, name='general-ledger'),
    path('transaction-detail/<slug:slug>/',views.transaction_details, name='transaction-details'),
    path('add-transaction/', views.add_general_ledger_trans.as_view(), name='add-transaction'),
    path('edit-transaction/<int:pk>/', views.edit_general_ledger_trans.as_view(), name='edit-transaction'),
]

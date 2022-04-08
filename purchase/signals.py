from django.db.models.signals import post_save
from .models import *

def invoice_payment(sender, instance, create, **kwargs):
    if created:
        Purchase.objects.create(
        invoice_id = instance.invoice_id,
        department = instance.department,
        vendor_name =instance. vendor,
        amount = instance.grand_total
        )
        
post_save.connect(invoice_payment, send)

from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.template.defaultfilters import slugify


# Create your models here.
class BakeryRmReturns(models.Model):
    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )

    CATEGORY = (
        ('Direct', 'Direct'),
        ('Indirect', 'Indirect'),
    )

    created_at = models.DateField("Date", default=now)
    
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Department')
    return_manager =  models.CharField(max_length=200, verbose_name = 'Procuement Manager')
    location =  models.CharField(max_length=200, verbose_name = 'Location')
    return_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Purchase Invoice Id")
    supplier =  models.CharField(max_length=200, verbose_name = 'Supplier')
    category=  models.CharField(max_length = 500, choices=CATEGORY, default='Direct', null = True, blank = True, verbose_name = 'Category')
    entry_measure =  models.CharField(max_length=200, verbose_name = 'Entry Measure')
    weight_pack =  models.CharField(max_length=200, verbose_name = 'Weight/Pack')
    product = models.CharField(max_length=200, verbose_name = 'Product')
    qty = models.FloatField(default=0.0, verbose_name = 'Quantity')
    unit_cost_price = models.FloatField(default=0.0, verbose_name = 'Unit Cost Price')
    total_cost_price = models.FloatField(default=0.0, verbose_name = 'Total Cost Price')


    @property
    def get_total_cost_price(self):
        return self.qty * self.unit_cost_price

    #@property
    #def get_discount_amount(self):
        #return self.discount * self.qty


    #@property
    #def get_net_amount(self):
        #return self.net_amount - self.total_amount_paid
    #---------------- Value Calculations -----------------#

    def save(self, *args, **kwargs):
        self.total_cost_price= self.get_total_cost_price
        #self.discount_value = self.get_discount_amount
        #self.net_amount = self.total_amount - self.discount_value

        super(BakeryRmReturns, self).save(*args, **kwargs)


    def __str__(self):
        return self.product

    class Meta():
        verbose_name = 'BakeryRmReturn'
        verbose_name_plural = 'BakeryRmReturns'
        ordering: ['date']


class BakeryRmDamages(models.Model):
    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )

    CATEGORY = (
        ('Direct', 'Direct'),
        ('Indirect', 'Indirect'),
    )

    created_at = models.DateField("Date", default=now)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Department')
    damage_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Purchase Invoice Id")
    category=  models.CharField(max_length = 500, choices=CATEGORY, default='Direct', null = True, blank = True, verbose_name = 'Category')
    entry_measure =  models.CharField(max_length=200, verbose_name = 'Entry Measure')
    weight_pack =  models.CharField(max_length=200, verbose_name = 'Weight/Pack')
    product = models.CharField(max_length=200, verbose_name = 'Product')
    qty = models.FloatField(default=0.0, verbose_name = 'Quantity')
    unit_cost_price = models.FloatField(default=0.0, verbose_name = 'Unit Cost Price')
    total_cost_price = models.FloatField(default=0.0, verbose_name = 'Total Cost Price')

    @property
    def get_total_cost_price(self):
        return self.qty * self.unit_cost_price

    #@property
    #def get_discount_amount(self):
        #return self.discount * self.qty

    #@property
    #def get_net_amount(self):
        #return self.net_amount - self.total_amount_paid
    #---------------- Value Calculations -----------------#
    def save(self, *args, **kwargs):
        self.total_cost_price= self.get_total_cost_price
        #self.discount_value = self.get_discount_amount
        #self.net_amount = self.total_amount - self.discount_value

        super(BakeryRmDamages, self).save(*args, **kwargs)


    def __str__(self):
        return self.product

    class Meta():
        verbose_name = 'BakeryRmDamage'
        verbose_name_plural = 'BakeryRmDamages'
        ordering: ['date']


class BakeryPurchase(models.Model):
    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )

    CATEGORY = (
        ('Direct', 'Direct'),
        ('Indirect', 'Indirect'),
    )

    created_at = models.DateField("Date", default=now)

    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Department')
    procuement_manager =  models.CharField(max_length=200, verbose_name = 'Procuement Manager')
    purchase_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Purchase Invoice Id")
    supplier =  models.CharField(max_length=200, verbose_name = 'Supplier')
    category=  models.CharField(max_length = 500, choices=CATEGORY, default='Direct', null = True, blank = True, verbose_name = 'Category')
    entry_measure =  models.CharField(max_length=200, verbose_name = 'Entry Measure')
    weight_pack =  models.CharField(max_length=200, verbose_name = 'Weight/Pack')
    product = models.CharField(max_length=200, verbose_name = 'Product')
    qty = models.FloatField(default=0.0, verbose_name = 'Quantity')
    unit_cost_price = models.FloatField(default=0.0, verbose_name = 'Unit Cost Price')
    total_cost_price = models.FloatField(default=0.0, verbose_name = 'Total Cost Price')


    @property
    def get_total_cost_price(self):
        return self.qty * self.unit_cost_price

    #@property
    #def get_discount_amount(self):
        #return self.discount * self.qty

    #---------------- Value Calculations -----------------#

    def save(self, *args, **kwargs):
        self.total_cost_price= self.get_total_cost_price
        #self.discount_value = self.get_discount_amount
        #self.net_amount = self.total_amount - self.discount_value

        super(BakeryPurchase, self).save(*args, **kwargs)


    def __str__(self):
        return self.product

    class Meta():
        verbose_name = 'BakeryPurchase'
        verbose_name_plural = 'BakeryPurchases'
        ordering: ['date']


class BakeryInventory(models.Model):
    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )

    SUBDEPARTMENTS = (
        ('Boulangerie Morning', 'Boulangerie Morning'),
        ('Boulangerie Evening', 'Boulangerie Evening'),
        ('Patisserie', 'Patisserie'),
    )
    STATUS = (
        ('Opening Stock', 'Opening Stock'),
        ('Closing Stock', 'Closing Stock'),

    )

    ENTRYMEASURE = (
        ('Grams', 'Grams'),
        ('Kg', 'Kg'),
        ('Unit', 'Unit'),
        ('Litre', 'Litre'),

    )

    DIRECT_INDIRECT = (
        ('Direct', 'Direct'),
        ('Indirect', 'Indirect'),
    )

    created_at = models.DateField("Date", default=now)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Department')
    sub_department =  models.CharField(max_length = 500, choices=SUBDEPARTMENTS, default='', null = True, blank = True, verbose_name = 'Sub Department')
    stock_status =  models.CharField(max_length = 500, choices=STATUS, default='', null = True, blank = True, verbose_name = 'Stock Status')
    direct_indirect = models.CharField(max_length = 500, verbose_name = 'Drect / Indirect', choices=DIRECT_INDIRECT, default='', null = True, blank = True,)
    entry_measure = models.CharField(max_length = 500, verbose_name = 'Entry Measure', choices=ENTRYMEASURE, default='', null = True, blank = True,)
    weight_per_pack = models.FloatField(default=0.0, verbose_name = 'Weight / Pack')
    product = models.CharField(max_length=200, verbose_name = 'Product')
    qty = models.FloatField(default=0.0, verbose_name = 'Quantity')
    unit_cost_price = models.FloatField(default=0.0, verbose_name = 'Unit Cost Price')
    total_cost_price = models.FloatField(default=0.0, verbose_name = 'Total Cost Price')

    @property
    def get_total_cost_price(self):
        return self.qty * self.unit_cost_price

    #@property
    #def get_discount_amount(self):
        #return self.discount * self.qty

    #---------------- Value Calculations -----------------#

    def save(self, *args, **kwargs):
        self.total_cost_price= self.get_total_cost_price
        super(BakeryInventory, self).save(*args, **kwargs)


    def __str__(self):
        return self.product

    class Meta():
        verbose_name = 'BakeryInventory'
        verbose_name_plural = 'BakeryInventory'
        ordering: ['date']


class BakeryOpeningBalances(models.Model):
    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )

    created_at = models.DateField("Date", default=now)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Department')
    openingbalance_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Opening Balance Id")
    customer = models.CharField(max_length=200, verbose_name = 'Customer')
    total_amount = models.FloatField(default=0.0, verbose_name = 'Amount')


    def __str__(self):
        return self.customer

#def post_save_settings_model_receiver(sender, instance, created, *args, **kwargs):
    #if created:
        #try:
            #UserSetting.objects.create(user=instance)
        #except:
            #pass
#post_save.connect(post_save_settings_model_receiver, sender= settings.AUTH_USER_MODEL)

    class Meta():
        verbose_name = 'BakeryOpeningBalance'
        verbose_name_plural = 'BakeryOpeningBalances'
        ordering: ['date']


class BakeryPayment(models.Model):

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )

    SESSIONS = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )

    COLLECTORS = (
        ('Moses', 'Moses'),
        ('Glory', 'Glory'),
        ('Kesty', 'Kesty'),
        ('Charles', 'Charles'),
        ('Cyril', 'Cyril'),
        ('Aly', 'Aly'),
        ('Joan', 'Joan'),
        ('Micheal', 'Micheal'),
        ('Esther', 'Esther'),
        ('Violet', 'Violet'),
        ('Kaba', 'Kaba'),
        ('Brenda', 'Brenda'),

    )

    created_at = models.DateField("Date", default=now)
    #employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Department')
    session = models.CharField(max_length = 500, choices=SESSIONS, default='', null = True, blank = True, verbose_name = 'Session')
    collector = models.CharField(max_length = 500, choices=COLLECTORS, null = True, blank = True, verbose_name = 'Collector')
    payment_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Payment Invoice Id")
    customer = models.CharField(max_length=200, verbose_name = 'Customer')
    amount = models.FloatField(default=0.0, verbose_name = 'Amount')

    def __str__(self):
        return self.customer

    class Meta():
        verbose_name = 'BakeryPayment'
        verbose_name_plural = 'BakeryPayments'
        ordering: ['date']


class BakeryReturn(models.Model):
    SUPPLIER = (
        ('Moses', 'Moses'),
        ('Glory', 'Glory'),
        ('Kesty', 'Kesty'),
    )

    CATEGORY = (
        ('Bread', 'Bread'),
        ('Confectionary', 'Confectionary'),
        ('Hamburger', 'Hamburger'),
        ('Sandwich', 'Sandwich'),
        ('Cake', 'Cake'),
        ('Milk Bread', 'Milk Bread'),
        ('Biscuit', 'Biscuit'),
        ('Croissant', 'Croissant'),
        ('Fruitage', 'Fruitage'),
    )

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )

    SUBDEPARTMENTS = (
        ('Boulangerie', 'Boulangerie'),
        ('Patisserie', 'Patisserie'),
    )

    SESSIONS = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )

    created_at = models.DateField("Date", default=now)
    #employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    return_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Return Invoice Id")
    invoice_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Invoice Id")
    customer_from = models.CharField(max_length=200, verbose_name = 'Customer_from')
    customer_to = models.CharField(max_length=200, verbose_name = 'Customer_to')
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Department')
    sub_department =  models.CharField(max_length = 500, choices=SUBDEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Sub Department')
    category = models.CharField(max_length = 500, choices=CATEGORY, default='', null = True, blank = True)
    product = models.CharField(max_length=200, verbose_name = 'Product Name')
    qty = models.FloatField(verbose_name = 'Quantity')
    cost_price = models.FloatField(default=0.0, verbose_name = 'Cost Price')
    total_amount = models.FloatField(default=0.0)

    @property
    def get_net_amount(self):
        return float(self.qty) * float(self.cost_price)

    #@property
    #def get_discount_amount(self):
        #return self.discount * self.qty

    #@property
    #def get_net_amount(self):
        #return self.net_amount - self.total_amount_paid
#---------------- Value Calculations -----------------#

    def save(self, *args, **kwargs):
        self.total_amount = self.get_net_amount
        #self.discount_value = self.get_discount_amount
        #self.net_amount = self.total_amount - self.discount_value

        super(BakeryReturn, self).save(*args, **kwargs)


    def __str__(self):
        return self.customer_from

    class Meta():
        verbose_name = 'BakeryReturns'
        verbose_name_plural = 'BakeryReturns'
        ordering: ['date']


class BakerySales(models.Model):
    SUPPLIER = (
        ('Moses', 'Moses'),
        ('Glory', 'Glory'),
        ('Kesty', 'Kesty'),
    )

    CATEGORY = (
        ('Bread', 'Bread'),
        ('Confectionary', 'Confectionary'),
        ('Hamburger', 'Hamburger'),
        ('Sandwich', 'Sandwich'),
        ('Cake', 'Cake'),
        ('Milk Bread', 'Milk Bread'),
        ('Biscuit', 'Biscuit'),
        ('Croissant', 'Croissant'),
        ('Fruitage', 'Fruitage'),
    )

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )

    SUBDEPARTMENTS = (
        ('Boulangerie', 'Boulangerie'),
        ('Patisserie', 'Patisserie'),
    )

    SESSIONS = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )

    created_at = models.DateField("Date", default=now)
    #employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    order_no =  models.IntegerField()
    invoice_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Invoice Id")
    supplier = models.CharField(max_length = 500, choices=SUPPLIER, default='', null = True, blank = True, verbose_name = 'Supplier')
    customer = models.CharField(max_length=200, verbose_name = 'Customer')
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Department')
    sub_department =  models.CharField(max_length = 500, choices=SUBDEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Sub Department')
    category = models.CharField(max_length = 500, choices=CATEGORY, default='', null = True, blank = True)
    session = models.CharField(max_length = 500, choices=SESSIONS, default='', null = True, blank = True, verbose_name = 'Session')
    product = models.CharField(max_length=200, verbose_name = 'Product Name')
    qty = models.FloatField(default=0.0, verbose_name = 'Quantity')
    cost_price = models.FloatField(default=0.0, verbose_name = 'Cost Price')
    total_amount = models.FloatField(default=0.0)
    discount = models.FloatField(default=0.0, verbose_name = 'Discount')
    discount_value = models.FloatField(default=0.0, verbose_name = 'Discount Value')
    net_amount = models.FloatField(default=0.0, verbose_name = 'Net Amount')
    commission = models.FloatField(default=0.0, verbose_name = 'Commission')

    @property
    def get_net_amount(self):
        return float(self.qty) * float(self.cost_price)

    @property
    def get_discount_amount(self):
        return float(self.discount) * float(self.qty)


    #@property
    #def get_net_amount(self):
        #return self.net_amount - self.total_amount_paid
#---------------- Value Calculations -----------------#

    def save(self, *args, **kwargs):
        self.total_amount = self.get_net_amount
        self.discount_value = self.get_discount_amount
        self.net_amount = self.total_amount - self.discount_value

        super(BakerySales, self).save(*args, **kwargs)


    def __str__(self):
        return self.supplier

    class Meta():
        verbose_name = 'BakerySales'
        verbose_name_plural = 'BakerySales'
        ordering: ['date']

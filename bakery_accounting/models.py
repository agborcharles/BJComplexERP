from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.template.defaultfilters import slugify


# Create your models here.
#------------------------------------------------------------------------------------------------#
class RawMaterials(models.Model):

    CATEGORY = (
        ('Direct', 'Direct'),
        ('Indirect', 'Indirect'),
    )

    product =  models.CharField(max_length = 500, default='', null = True, blank = True, verbose_name = 'Product Name')
    category=  models.CharField(max_length = 500, choices=CATEGORY, default='Direct', null = True, blank = True, verbose_name = 'Category')
    weight_pack =  models.CharField(max_length=200, verbose_name = 'Weight/Pack')
    entry_measure =  models.CharField(max_length=200, verbose_name = 'Entry Measure')
    cost_price = models.FloatField(default=0.0, verbose_name = 'Unit Cost Price')
    packaging =  models.CharField(max_length = 500, default='', null = True, blank = True, verbose_name = 'Packaging')


    def __str__(self):
        return self.product

    class Meta():
        verbose_name = 'Products Raw Material'
        verbose_name_plural = 'Products Raw Materials'

#------------------------------------------------------------------------------------------------#

class Quarter(models.Model):

    quarter_name =  models.CharField(max_length = 500,  null = True, blank = True, verbose_name = 'Cquarter_name')

    def __str__(self):
        return self.quarter_name

    class Meta():
        verbose_name = 'Quarter'
        verbose_name_plural = 'Quarter'

class BakeryCustomers(models.Model):

    CUSTOMER_TYPE = (
        ('Random Customer', 'Random Customer'),
        ('Others', 'Others'),
        ('Company', 'Company'),
        ('Sole Proprietor', 'Sole Proprietor'),
        ('Supplier', 'Supplier'),
        ('Institutions', 'Institutions'),
    )

    created_at = models.DateField("Date", default=now)
    customer =  models.CharField(max_length = 500,  null = True, blank = True, verbose_name = 'Customers')
    busness_type =  models.CharField(max_length = 500, choices=CUSTOMER_TYPE,  null = True, blank = True, verbose_name = 'busness_type')
    quarter=  models.CharField(max_length = 500, default="",  null = True, blank = True, verbose_name = 'quarter')
    street =  models.CharField(max_length = 500, default="",  null = True, blank = True, verbose_name = 'street')
    gps_long =  models.FloatField(max_length = 500, default="",  null = True, blank = True, verbose_name = 'gps_long')
    gps_lat =  models.FloatField(max_length = 500, default="",  null = True, blank = True, verbose_name = 'gps_lat')
    address = models.CharField(max_length = 500, default="",  null = True, blank = True, verbose_name = 'Address')
    phone_1 =  models.CharField(max_length = 500, default="",  null = True, blank = True, verbose_name = 'phone_1')
    phone_2 =  models.CharField(max_length = 500, default="",  null = True, blank = True, verbose_name = 'phone_2')
    road_street_location =  models.CharField(max_length = 500, default="",  null = True, blank = True, verbose_name = 'Road Street Location')

    def __str__(self):
        return self.customer

    class Meta():
        verbose_name = 'Bakery Customers'
        verbose_name_plural = 'Bakery Customers'


# Create your models here.


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
        verbose_name = 'Bakery Raw Material Damage'
        verbose_name_plural = 'Bakery Raw Material Damages'
        ordering: ['date']


class BakeryPurchase(models.Model):
    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )

    CATEGORY = (
        ('Direct', 'Direct'),
        ('Indirect', 'Indirect'),
    )

    Stock_STATUS = (
        ('Return Inwards', 'Return Inwards'),
        ('Return Outwards', 'Return Outwards'),
        ('Damages', 'Damages'),
        ('Purchases', 'Purchases'),
    )

    created_at = models.DateField("Date", default=now)

    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Department')
    procuement_manager =  models.CharField(max_length=200, verbose_name = 'Procuement Manager')
    purchase_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Purchase Invoice Id")
    location = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Location")
    supplier =  models.CharField(max_length=200, verbose_name = 'Supplier')
    stock_status =  models.CharField(max_length = 500, choices=Stock_STATUS, default='', null = True, blank = True, verbose_name = 'Stock Status')
    category=  models.CharField(max_length = 500, choices=CATEGORY, default='Direct', null = True, blank = True, verbose_name = 'Location')
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
        verbose_name = 'Bakery Purchase'
        verbose_name_plural = 'Bakery Purchases'
        ordering: ['date']
#---------------------------------------------------------------------#
class BakeryMagazineDistribution(models.Model):

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )

    SUBDEPARTMENTS = (
        ('Boulangerie Morning', 'Boulangerie Morning'),
        ('Boulangerie Evening', 'Boulangerie Evening'),
        ('Patisserie Morning', 'Patisserie Morning'),
        ('Patisserie Evening', 'Patisserie Evening'),

    )

    CATEGORY = (
        ('Direct', 'Direct'),
        ('Indirect', 'Indirect'),
    )

    created_at = models.DateField("Date", default=now)

    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Department')
    sub_department =  models.CharField(max_length = 500, choices=SUBDEPARTMENTS, default='', null = True, blank = True, verbose_name = 'Sub Department')
    sub_department_manager =  models.CharField(max_length=200, null = True, blank = True, verbose_name = 'Sub Department Manager')
    distribution_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Distribution Id")
    stock_manager =  models.CharField(max_length=200, null = True, blank = True, verbose_name = 'Stock Manager')
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

        super(BakeryMagazineDistribution, self).save(*args, **kwargs)


    def __str__(self):
        return self.product

    class Meta():
        verbose_name = 'Bakery Magazine Distribution'
        verbose_name_plural = 'Bakery Magazine Distribution'
        ordering: ['date']

#----------------------------------------------------------------#

#----------------------------------------------------------------#
class BakeryInventoryMagazine(models.Model):
    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )

    SUBDEPARTMENTS = (
        ('Boulangerie Morning', 'Boulangerie Morning'),
        ('Boulangerie Evening', 'Boulangerie Evening'),
        ('Patisserie Morning', 'Patisserie Morning'),
        ('Patisserie Evening', 'Patisserie Evening'),
        ('Magazine', 'Magazine'),

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
        super(BakeryInventoryMagazine, self).save(*args, **kwargs)


    def __str__(self):
        return self.product

    class Meta():
        verbose_name = 'Bakery Inventory Magazine'
        verbose_name_plural = 'Bakery Inventory Magazine'
        ordering: ['date']
#--------------------------------------------------------------#
class BakeryInventorySubDepartments(models.Model):
    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )

    SUBDEPARTMENTS = (
        ('Boulangerie Morning', 'Boulangerie Morning'),
        ('Boulangerie Evening', 'Boulangerie Evening'),
        ('Patisserie Morning', 'Patisserie Morning'),
        ('Patisserie Evening', 'Patisserie Evening'),
        ('All', 'All'),

    )
    STATUS = (
        ('Opening Stock', 'Opening Stock'),
        ('Closing Stock', 'Closing Stock'),
        ('Returns', 'Returns'),
        ('Transfer Inwards', 'Transfer Inwards'),
        ('Transfer Outwards', 'Transfer Outwards'),
        ('Damages', 'Damages'),
        ('Added Stock', 'Added Stock'),
        ('Rm Usage', 'Rm Usage'),

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
    supervisor =  models.CharField(max_length = 500,  default='', null = True, blank = True, verbose_name = 'Supervisor')
    stock_status =  models.CharField(max_length = 500, choices=STATUS, default='', null = True, blank = True, verbose_name = 'Stock Status')
    sub_department_transfers =  models.CharField(max_length = 500, choices=SUBDEPARTMENTS, default='', null = True, blank = True, verbose_name = 'Sub Department Transfers')
    category = models.CharField(max_length = 500, verbose_name = 'Category', choices=DIRECT_INDIRECT, default='', null = True, blank = True,)
    weight_per_pack = models.FloatField(default=0.0, verbose_name = 'Weight / Pack')
    entry_measure = models.CharField(max_length = 500, verbose_name = 'Entry Measure', choices=ENTRYMEASURE, default='', null = True, blank = True,)
    product = models.CharField(max_length=200, verbose_name = 'Product')
    qty = models.FloatField(default=0.0, verbose_name = 'Quantity')
    rm_total_weight_grams = models.FloatField(default=0.0, verbose_name = 'RM Total Weight (Grams)')
    unit_cost_price = models.FloatField(default=0.0, verbose_name = 'Unit Cost Price')
    total_cost_price = models.FloatField(default=0.0, verbose_name = 'Total Cost Price')

    @property
    def get_total_cost_price(self):
        return self.qty * self.unit_cost_price
    @property
    def get_rm_total_weight_grams(self):
        return float(self.qty) * float(self.weight_per_pack)

    #@property
    #def get_discount_amount(self):
        #return self.discount * self.qty

    #---------------- Value Calculations -----------------#

    def save(self, *args, **kwargs):
        self.total_cost_price= self.get_total_cost_price
        self.rm_total_weight_grams= self.get_rm_total_weight_grams
        super(BakeryInventorySubDepartments, self).save(*args, **kwargs)

    def __str__(self):
        return self.product

    class Meta():
        verbose_name = 'Bakery Inventory Sub Departments'
        verbose_name_plural = 'Bakery Inventory Sub Departments'
        ordering: ['date']

class BakeryRmUsageSubDepartments(models.Model):
    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )

    SUBDEPARTMENTS = (
        ('Boulangerie Morning', 'Boulangerie Morning'),
        ('Boulangerie Evening', 'Boulangerie Evening'),
        ('Patisserie Morning', 'Patisserie Morning'),
        ('Patisserie Evening', 'Patisserie Evening'),
        ('All', 'All'),

    )
    STATUS = (
        ('Opening Stock', 'Opening Stock'),
        ('Closing Stock', 'Closing Stock'),
        ('Returns', 'Returns'),
        ('Transfer Inwards', 'Transfer Inwards'),
        ('Transfer Outwards', 'Transfer Outwards'),
        ('Damages', 'Damages'),
        ('Added Stock', 'Added Stock'),

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


    SESSIONS = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )

    MIXTURES = (
        ('First Mixture', 'First Mixture'),
        ('Second Mixture', 'Second Mixture'),
        ('Third Mixture', 'Third Mixture'),
        ('Fourth Mixture', 'Fourth Mixture'),
        ('Fifth Mixture', 'Fifth Mixture'),
        ('Sixth Mixture', 'Sixth Mixture'),
        ('Seventh Mixture', 'Seventh Mixture'),
        ('Eight Mixture', 'Eight Mixture'),
        ('Ninth Mixture', 'Ninth Mixture'),
        ('Tenth Mixture', 'Tenth Mixture'),
        ('Eleventh Mixture', 'Eleventh Mixture'),
        ('Twelfth Mixture', 'Twelfth Mixture'),

    )



    created_at = models.DateField("Date", default=now)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Department')
    sub_department =  models.CharField(max_length = 500, choices=SUBDEPARTMENTS, default='', null = True, blank = True, verbose_name = 'Sub Department')
    status =  models.CharField(max_length = 500, default='Rm Usage', null = True, blank = True, verbose_name = 'Status')
    session = models.CharField(max_length = 500, choices=SESSIONS, default='', null = True, blank = True, verbose_name = 'Session')
    mixture_number =  models.CharField(max_length = 500, choices=MIXTURES, default='', null = True, blank = True, verbose_name = 'Mixture Number')
    supervisor =  models.CharField(max_length = 500,  default='', null = True, blank = True, verbose_name = 'Supervisor')
    product = models.CharField(max_length=200, verbose_name = 'Product')
    category = models.CharField(max_length = 500, verbose_name = 'Category', choices=DIRECT_INDIRECT, default='', null = True, blank = True,)
    weight_per_pack = models.FloatField(default=0.0, verbose_name = 'Weight / Pack')
    entry_measure = models.CharField(max_length = 500, verbose_name = 'Entry Measure', choices=ENTRYMEASURE, default='', null = True, blank = True,)
    qty = models.FloatField(default=0.0, verbose_name = 'Quantity')
    rm_total_weight_grams = models.FloatField(default=0.0, verbose_name = 'RM Total Weight (Grams)')
    unit_cost_price = models.FloatField(default=0.0, verbose_name = 'Unit Cost Price')
    total_cost_price = models.FloatField(default=0.0, verbose_name = 'Total Cost Price')

    @property
    def get_total_cost_price(self):
        return self.qty * self.unit_cost_price
    @property
    def get_rm_total_weight_grams(self):
        return float(self.qty) * float(self.weight_per_pack)

    #@property
    #def get_discount_amount(self):
        #return self.discount * self.qty

    #---------------- Value Calculations -----------------#

    def save(self, *args, **kwargs):
        self.total_cost_price= self.get_total_cost_price
        self.rm_total_weight_grams= self.get_rm_total_weight_grams
        super(BakeryRmUsageSubDepartments, self).save(*args, **kwargs)



    def __str__(self):
        return self.product


    class Meta():
        verbose_name = 'Bakery Raw Material Usage Sub-Departments'
        verbose_name_plural = 'Bakery Raw Material Usage Sub-Departments'
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
        verbose_name = 'Bakery Opening Balance'
        verbose_name_plural = 'Bakery Opening Balances'
        ordering: ['date']


class BakeryPayment(models.Model):

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )

    SESSIONS = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )

    PAYMENTMODE = (
        ('Cash', 'Cash'),
        ('Mobile Money', 'Mobile Money'),
        ('Bank', 'Bank'),
        ('Cheque', 'Cheque'),
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
        ('Akem', 'Akem'),
        ('Boulangerie Counter', 'Boulangerie Counter'),
        ('Naomi', 'Naomi'),
        ('Nana', 'Nana'),
        ('Glen', 'Glen'),

    )

    created_at = models.DateField("Date", default=now)
    #employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Department')
    quarter = models.CharField(max_length=200, default='', null = True, blank = True, verbose_name = 'Quarter')
    street = models.CharField(max_length=200, default='', null = True, blank = True, verbose_name = 'Street')
    session = models.CharField(max_length = 500, choices=SESSIONS, default='', null = True, blank = True, verbose_name = 'Session')
    collector = models.CharField(max_length = 500, choices=COLLECTORS, null = True, blank = True, verbose_name = 'Collector')
    payment_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Payment Invoice Id")
    customer = models.CharField(max_length=200, verbose_name = 'Customer')
    amount = models.FloatField(default=0.0, verbose_name = 'Amount')
    payment_mode = models.CharField(max_length=200,  choices=PAYMENTMODE, default="", null = True, blank = True, verbose_name = 'Payment Mode')

    def __str__(self):
        return self.customer

    class Meta():
        verbose_name = 'Bakery Payment'
        verbose_name_plural = 'Bakery Payments'
        ordering: ['date']


class BakeryReturn(models.Model):
    SUPPLIER = (
        ('Moses', 'Moses'),
        ('Glory', 'Glory'),
        ('Kesty', 'Kesty'),
        ('Adjusment', 'Adjusment'),
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
        verbose_name = 'Bakery Returns'
        verbose_name_plural = 'Bakery Returns'
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
        verbose_name = 'Bakery Sales'
        verbose_name_plural = 'Bakery Sales'
        ordering: ['date']

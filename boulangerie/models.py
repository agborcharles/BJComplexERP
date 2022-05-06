from django.db import models
import datetime
from django.utils.timezone import now
# Create your models here.
class BoulangerieProducts(models.Model):
    SUBDEPARTMENTS = (
        ('Boulangerie', 'Boulangerie'),
        ('Patisserie', 'Patisserie'),
    )

    product =  models.CharField(max_length=200, verbose_name = 'Product')
    category = models.CharField(max_length=200, verbose_name = 'Category')
    sub_department =  models.CharField(max_length = 500, choices=SUBDEPARTMENTS, default='', null = True, blank = True, verbose_name = 'Sub Department')
    #---------------- Value Calculations -----------------#

    def __str__(self):
        return self.sub_department

    class Meta():
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering: ['-created_at']

class BoulangerieSubDepartment(models.Model):
    SUBDEPARTMENTS = (
        ('Boulangerie', 'Boulangerie'),
        ('Patisserie', 'Patisserie'),
    )
    sub_department =  models.CharField(max_length = 500, choices=SUBDEPARTMENTS, default='', null = True, blank = True, verbose_name = 'Sub Department')
    #---------------- Value Calculations -----------------#

    def __str__(self):
        return self.sub_department

    class Meta():
        verbose_name = 'Sub Department'
        verbose_name_plural = 'Sub Departments'
        ordering: ['-created_at']


class Sessions(models.Model):
    SESSIONS = (
        ('1st Session', '1st Session'),
        ('2nd Session', '2nd Session'),
    )

    session =  models.CharField(max_length = 500, choices=SESSIONS, default='', null = True, blank = True, verbose_name = 'Session')
    #---------------- Value Calculations -----------------#

    def __str__(self):
        return self.session

    class Meta():
        verbose_name = 'Session'
        verbose_name_plural = 'Sessions'
        #ordering: ['-created_at']


class BoulangerieLedger(models.Model):
    SESSIONS = (
        ('1st Session', '1st Session'),
        ('2nd Session', '2nd Session'),
    )

    STOCKSTATUS = (
        ('Purchases', 'Purchases'),

    )
    DEPARTMENTS = (
        ('Boulangerie', 'Boulangerie'),

    )

    created_at = models.DateField("Date", default=now)
    session =  models.CharField(max_length = 500, choices=SESSIONS, default='', null = True, blank = True, verbose_name = 'Session')
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Boualangerie', null = True, blank = True, verbose_name = 'Department')
    employee =  models.CharField(max_length = 500, default='', null = True, blank = True, verbose_name = 'Employee')
    description =  models.CharField(max_length=200, verbose_name = 'Description')
    amount = models.FloatField(default=0.0, verbose_name = 'Amount')
    accounts_dr = models.CharField(max_length=200, default='', null = True, blank = True, verbose_name = 'Account Debit')
    accounts_cr = models.CharField(max_length=200, default='', null = True, blank = True, verbose_name = 'AccountsCredit')


    def __str__(self):
        return self.department

    class Meta():
        verbose_name = 'Boulangerie Ledger'
        verbose_name_plural = 'Boulangerie Ledger'
        ordering: ['-created_at']




class BoulangerieInventory(models.Model):
    SESSIONS = (
        ('1st Session', '1st Session'),
        ('2nd Session', '2nd Session'),
    )

    STOCKSTATUS = (
        ('Opening Stock', 'Opening Stock'),
        ('Closing Stock', 'Closing Stock'),

    )
    DEPARTMENTS = (
        ('Boulangerie', 'Boulangerie'),

    )
    SUBDEPARTMENTS = (
        ('Boulangerie', 'Boulangerie'),
        ('Patisserie', 'Patisserie'),
    )

    created_at = models.DateField("Date", default=now)
    session =  models.CharField(max_length = 500, choices=SESSIONS, default='', null = True, blank = True, verbose_name = 'Session')
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Boualangerie', null = True, blank = True, verbose_name = 'Department')
    employee =  models.CharField(max_length = 500, default='', null = True, blank = True, verbose_name = 'Employee')
    stock_status =  models.CharField(max_length = 500, choices=STOCKSTATUS, default='', null = True, blank = True, verbose_name = 'Stock Status')
    sub_department =  models.CharField(max_length = 500, choices=SUBDEPARTMENTS, default='', null = True, blank = True, verbose_name = 'Sub Department')
    product =  models.CharField(max_length=200, verbose_name = 'Product')
    qty=  models.FloatField(default=0.0, verbose_name = 'Quantity')
    unit_cost_price = models.FloatField(default=0.0, verbose_name = 'Unit Cost Price')
    unit_selling_price = models.FloatField(default=0.0, verbose_name = 'Unit Selling Price')
    total_cost_price = models.FloatField(default=0.0, verbose_name = 'Total Cost Price')
    total_selling_price = models.FloatField(default=0.0, verbose_name = 'Total Selling Price')
    gross_profit = models.FloatField(default=0.0, verbose_name = 'Gross Profit')
    margin = models.FloatField(default=0.0, verbose_name = 'margin')

    @property
    def get_total_cost_price(self):
        return self.qty * self.unit_cost_price

    @property
    def get_total_selling_price(self):
        return self.qty * self.unit_selling_price

    @property
    def get_gross_profit(self):
        return self.total_selling_price - self.total_cost_price

    @property
    def get_margin(self):
        return self.gross_profit / self.unit_selling_price
    #---------------- Value Calculations -----------------#

    def save(self, *args, **kwargs):
        self.total_cost_price= self.get_total_cost_price
        self.total_selling_price= self.get_total_selling_price
        self.gross_profit= self.get_gross_profit
        self.margin= self.get_margin

        super(BoulangerieInventory, self).save(*args, **kwargs)



    def __str__(self):
        return self.department

    class Meta():
        verbose_name = 'Boulangerie Inventory'
        verbose_name_plural = 'Boulangerie Inventory'
        ordering: ['-created_at']

class BoulangerieReturnsDamages(models.Model):
    SESSIONS = (
        ('1st Session', '1st Session'),
        ('2nd Session', '2nd Session'),
    )

    STOCKSTATUS = (
        ('Returns', 'Returns'),
        ('Damages', 'Damages'),

    )
    DEPARTMENTS = (
        ('Boulangerie', 'Boulangerie'),
        ('Patisserie', 'Patisserie'),
    )
    SUBDEPARTMENTS = (
        ('Boulangerie', 'Boulangerie'),
        ('Patisserie', 'Patisserie'),
    )

    created_at = models.DateField("Date", default=now)
    session =  models.CharField(max_length = 500, choices=SESSIONS, default='', null = True, blank = True, verbose_name = 'Session')
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Boualangerie', null = True, blank = True, verbose_name = 'Department')
    employee =  models.CharField(max_length = 500, default='', null = True, blank = True, verbose_name = 'Employee')
    stock_status =  models.CharField(max_length = 500, choices=STOCKSTATUS, default='', null = True, blank = True, verbose_name = 'Stock Status')
    sub_department =  models.CharField(max_length = 500, choices=SUBDEPARTMENTS, default='', null = True, blank = True, verbose_name = 'Sub Department')
    product =  models.CharField(max_length=200, verbose_name = 'Product')
    qty=  models.FloatField(default=0.0, verbose_name = 'Quantity')
    unit_cost_price = models.FloatField(default=0.0, verbose_name = 'Unit Cost Price')
    unit_selling_price = models.FloatField(default=0.0, verbose_name = 'Unit Selling Price')
    total_cost_price = models.FloatField(default=0.0, verbose_name = 'Total Cost Price')
    total_selling_price = models.FloatField(default=0.0, verbose_name = 'Total Selling Price')
    gross_profit = models.FloatField(default=0.0, verbose_name = 'Gross Profit')
    margin = models.FloatField(default=0.0, verbose_name = 'margin')

    @property
    def get_total_cost_price(self):
        return self.qty * self.unit_cost_price

    @property
    def get_total_selling_price(self):
        return self.qty * self.unit_selling_price

    @property
    def get_gross_profit(self):
        return self.total_selling_price - self.total_cost_price

    @property
    def get_margin(self):
        return self.gross_profit / self.unit_selling_price
    #---------------- Value Calculations -----------------#

    def save(self, *args, **kwargs):
        self.total_cost_price= self.get_total_cost_price
        self.total_selling_price= self.get_total_selling_price
        self.gross_profit= self.get_gross_profit
        self.margin= self.get_margin

        super(BoulangerieReturnsDamages, self).save(*args, **kwargs)



    def __str__(self):
        return self.department

    class Meta():
        verbose_name = 'Boulangerie-Returns-Damages'
        verbose_name_plural = 'Boulangerie-Returns-Damages'
        ordering: ['-created_at']


class BoulangeriePurchases(models.Model):
    SESSIONS = (
        ('1st Session', '1st Session'),
        ('2nd Session', '2nd Session'),
    )

    STOCKSTATUS = (
        ('Purchases', 'Purchases'),

    )
    DEPARTMENTS = (
        ('Boulangerie', 'Boulangerie'),

    )
    SUBDEPARTMENTS = (
        ('Boulangerie', 'Boulangerie'),
        ('Patisserie', 'Patisserie'),
    )

    created_at = models.DateField("Date", default=now)
    session =  models.CharField(max_length = 500, choices=SESSIONS, default='', null = True, blank = True, verbose_name = 'Session')
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Boualangerie', null = True, blank = True, verbose_name = 'Department')
    sub_department =  models.CharField(max_length = 500, choices=SUBDEPARTMENTS, default='', null = True, blank = True, verbose_name = 'Sub Department')
    stock_status =  models.CharField(max_length = 500, choices=STOCKSTATUS, default='', null = True, blank = True, verbose_name = 'Stock Status')
    employee =  models.CharField(max_length = 500, default='', null = True, blank = True, verbose_name = 'Employee')
    product =  models.CharField(max_length=200, verbose_name = 'Product')
    qty=  models.FloatField(default=0.0, verbose_name = 'Quantity')
    unit_cost_price = models.FloatField(default=0.0, verbose_name = 'Unit Cost Price')
    unit_selling_price = models.FloatField(default=0.0, verbose_name = 'Unit Selling Price')
    total_cost_price = models.FloatField(default=0.0, verbose_name = 'Total Cost Price')
    total_selling_price = models.FloatField(default=0.0, verbose_name = 'Total Selling Price')
    gross_profit = models.FloatField(default=0.0, verbose_name = 'Gross Profit')
    margin = models.FloatField(default=0.0, verbose_name = 'margin')

    @property
    def get_total_cost_price(self):
        return self.qty * self.unit_cost_price

    @property
    def get_total_selling_price(self):
        return self.qty * self.unit_selling_price

    @property
    def get_gross_profit(self):
        return self.total_selling_price - self.total_cost_price

    @property
    def get_margin(self):
        return self.gross_profit / self.unit_selling_price
    #---------------- Value Calculations -----------------#

    def save(self, *args, **kwargs):
        self.total_cost_price= self.get_total_cost_price
        self.total_selling_price= self.get_total_selling_price
        self.gross_profit= self.get_gross_profit
        self.margin= self.get_margin

        super(BoulangeriePurchases, self).save(*args, **kwargs)



    def __str__(self):
        return self.department

    class Meta():
        verbose_name = 'Boulangerie Purchases'
        verbose_name_plural = 'Boulangerie Purchases'
        ordering: ['-created_at']

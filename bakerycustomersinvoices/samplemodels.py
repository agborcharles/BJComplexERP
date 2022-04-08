
class Department(models.Model):
    name = models.CharField(max_length=100, default='')
    created = models.DateField(default=now)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

class Category(models.Model):
    name = models.CharField(max_length=100, default='')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank =True)
    created = models.DateField(default=now)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=100, default='', unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=1, null = True, blank = True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    created = models.DateField(default=now)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


def increment_invoice_number():
    last_invoice = Invoice.objects.all().order_by('id').last()
    today = datetime.date.today()
    today_string = today.strftime("%Y-%m-%d")

    if not last_invoice:
            return today_string + "-" + 'INV0001'

    invoice_id = last_invoice.invoice_id
    invoice_int = int(invoice_id.split('INV000')[-1])
    new_invoice_int = invoice_int + 1

    new_invoice_id = today_string + "-" + 'INV000'  + str(new_invoice_int)
    return new_invoice_id


class Invoice(models.Model):
    created = models.DateField(default=now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice_id = models.CharField(max_length = 500,default=increment_invoice_number, null = True, blank = True)
    sales_person = models.CharField(max_length = 500, null = True, blank = True, default='')
    # Total field for each invoice
    vat_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    #grand_total = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    due_date = models.DateField(default=now)
    def __str__(self):
        return self.invoice_id

    @property
    def is_past_due(self):
        return date.today() > self.due_date

    @property
    def total_amount(self):
        return sum([item.get_net_amount for item in self.invoiceitem_set.all()])
        return

    @property
    def get_grand_total(self):
        return sum([item.get_net_amount for item in self.invoiceitem_set.all()]) + self.vat_amount
        return

    @property
    def get_total_amount_paid(self):
        return sum([item.amount_paid for item in self.invoicepayment_set.all()])



        def save(self, *args, **kwargs):
            self.grand_total = self.get_grand_total
            #self.invoice.save()
            super().save(*args, **kwargs)

class InvoiceItem(models.Model):
    Sales_Session = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )
    created = models.DateField(default=now)
    sales_session =  models.CharField(max_length = 500, choices=Sales_Session,  default='Morning', null = True, blank = True)
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    price = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    discount = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    total_discount = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    total_amount = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    net_amount = models.DecimalField(max_digits=20, decimal_places=0, default=0)


    @property
    def get_total_amount(self):
        return (Decimal(self.quantity) * Decimal(self.price)) - (Decimal(self.quantity) * Decimal(self.discount))

    @property
    def get_total_discount(self):
        return (Decimal(self.quantity) * Decimal(self.discount))

    @property
    def get_net_amount(self):
        return (Decimal(self.get_total_amount) - Decimal(self.get_total_discount))
    # Overriding the save method to update invoice total for each new item
    def save(self, *args, **kwargs):
        self.price = self.product.price

        self.total_discount = self.get_total_discount
        self.total_amount = self.get_total_amount
        self.net_amount = self.get_net_amount
        #self.total_amount = order_items.aggregate(Sum('total_price'))['total_price__sum'] if order_items.exists() else 0.00
        #self.invoice.save()
        super().save(*args, **kwargs)


def increment_invoice_number():
    last_invoice_payment = InvoicePayment.objects.all().order_by('id').last()
    today = datetime.date.today()
    today_string = today.strftime("%Y-%m-%d")

    if not last_invoice_payment:
            return today_string + "-" + 'PAYMT0001'

    payment_id = last_invoice_payment.payment_id
    payment_int = int(payment_id.split('PAYMT000')[-1])
    new_payment_int = payment_int + 1

    new_payment_id = today_string + "-" + 'PAYMT000'  + str(new_payment_int)
    return new_payment_id

class InvoicePayment(models.Model):
    Payment_Installment = (
        ('1st Installment', '1st Installment'),
        ('2nd Installment', '2nd Installment'),
        ('3rd Installment', '3rd Installment'),
        ('4th Installment', '4th Installment'),
        ('5th Installment', '5th Installment'),
        ('6th Installment', '6th Installment'),
        ('7th Installment', '7th Installment'),
        ('8th Installment', '8th Installment'),
        ('9th Installment', '9th Installment'),
        ('10th Installment', '10th Installment'),

    )

    Payment_Session = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )
    created = models.DateField(default=now)
    payment_session =  models.CharField(max_length = 500, choices=Payment_Session,  default='Morning', null = True, blank = True)
    payment_installment =  models.CharField(max_length = 500, choices=Payment_Installment,  default='1st Installment', null = True, blank = True)
    employee = models.CharField(max_length = 500, null = True, blank = True, default='')
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    payment_id = models.CharField(max_length = 500,default=increment_invoice_number, null = True, blank = True)

    def __str__(self):
        return self.payment_id

def payment_signal(sender, **kwargs):
    if kwargs['created']:
        payment_signal_trans = InvoicePayment.objects.create(invoice=kwargs['instance'])

post_save.connect(payment_signal, sender=Invoice)




class OpeningBalance(models.Model):
    created = models.DateField(default=now)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.customer)

    class Meta:
        ordering = ['-created']

# ---- OpeningBalance Signal ---- #
def opening_balance(sender, **kwargs):
    if kwargs['created']:
        opening_balance_trans = OpeningBalance.objects.create(customer=kwargs['instance'])

post_save.connect(opening_balance, sender=Customer)


def increment_invoice_number():
    last_return_products = OpeningReturn.objects.all().order_by('id').last()
    today = datetime.date.today()
    today_string = today.strftime("%Y-%m-%d")

    if not last_return_products:
            return today_string + "-" + 'RET0001'

    return_id = last_return_products.return_id
    return_int = int(return_id.split('RET000')[-1])
    new_return_int = return_int + 1

    new_return_id = today_string + "-" + 'RET000'  + str(new_return_int)
    return new_return_id

class OpeningReturn(models.Model):
    SALES_SESSION = (
                ('Morning', 'Morning'),
                ('Evening', 'Evening'),
                )
    created = models.DateField(default=now)
    sales_session = models.CharField(max_length=100, choices=SALES_SESSION, default='Morning')
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    return_id = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    price = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    discount = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    total_return_discount = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    total_return_amount = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    net_return_amount = models.DecimalField(max_digits=20, decimal_places=0, default=0)

    def __str__(self):
        return str(self.customer)

    class Meta:
        ordering = ['-created']

    @property
    def get_amount(self):
        virtual_qty = 0
        if self.amount:
            return self.amount + 0
        else:
            return virtual_qty * self.amount
            return

    def save(self, *args, **kwargs):
        self.amount = self.get_amount
        super(OpeningReturn, self).save(*args, **kwargs)


# ---- Return Signal ---- #

#def return_signal(sender, **kwargs):
    #if kwargs['created']:
        #return_signal_trans = OpeningReturn.objects.create(customer=kwargs['instance'])

#post_save.connect(return_signal, sender=Customer)


class OpeningDamage(models.Model):
    created = models.DateField(default=now)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, default=3)
    transaction_status = models.CharField(max_length=100, default='Bakery Damages')
    slug = models.SlugField(max_length=100, unique=True, blank=True, default=uuid.uuid4)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.customer)

    class Meta:
        ordering = ['-created']


    @property
    def get_amount(self):
        virtual_qty = 0
        if self.amount:
            return self.amount + 0
        else:
            return virtual_qty * self.amount
            return

    def save(self, *args, **kwargs):
        self.amount = self.get_amount
        super(OpeningDamage, self).save(*args, **kwargs)


# ---- Return Signal ---- #

#def damage_signal(sender, **kwargs):
    #if kwargs['created']:
        #damage_signal_trans = OpeningDamage.objects.create(customer=kwargs['instance'])

#post_save.connect(damage_signal, sender=Customer)

class CommissionEarned(models.Model):
    created = models.DateField(default=now)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    transaction_status = models.CharField(max_length=100, default='Commission Earned')
    slug = models.SlugField(max_length=100, unique=True, blank=True, default=uuid.uuid4)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.customer)

    class Meta:
        ordering = ['-created']

    @property
    def get_amount(self):
        virtual_qty = 0
        if self.amount:
            return self.amount + 0
        else:
            return virtual_qty * self.amount
            return

    def save(self, *args, **kwargs):
        self.amount = self.get_amount
        super(CommissionEarned, self).save(*args, **kwargs)

# ---- Return Signal ---- #

#def commission_signal(sender, **kwargs):
    #if kwargs['created']:
        #commission_signal_trans = CommissionEarned.objects.create(customer=kwargs['instance'])

#post_save.connect(commission_signal, sender=Customer)


# class Interest(models.Model):
#     client = models.ForeignKey(#Client, on_delete=models.CASCADE, related_name='interests',)
#     amount = models.DecimalField(decimal_places=2, max_digits=15, validators=[
#                                  MinValueValidator(Decimal('10.00'))])
#     transaction_time = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.client)


from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(CommissionEarned)
class CommissionEarnedAdmin(admin.ModelAdmin):
    list_display = [  'created', 'customer', 'amount', 'slug', ]


@admin.register(OpeningReturn)
class OpeningReturnAdmin(admin.ModelAdmin):
    list_display = [  'created', 'sales_session', 'return_id', 'product', 'quantity',
                    'total_return_amount', 'total_return_discount', 'net_return_amount' ]

@admin.register(OpeningDamage)
class OpeningDamageAdmin(admin.ModelAdmin):
    list_display = [  'created', 'customer', 'amount', 'slug', ]


@admin.register(OpeningBalance)
class OpeningBalanceAdmin(ImportExportModelAdmin):
    list_display = ['created',  'customer', 'amount' ]


class CustomerAdmin(ImportExportModelAdmin):
    list_display = [ 'id', 'created', 'customer_name', 'account_number', 'slug',
                    'customer_type', 'is_active', ]
    # search list
    search_fields = ['customer_name']


class DepartmentAdmin(ImportExportModelAdmin):
    list_display = ['id','created', 'name',  ]

class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['id','created', 'name', 'department' ]
    list_editable = ('name',)


class ProductAdmin(ImportExportModelAdmin):
    list_display = ['id','created', 'category', 'name', 'price',]
    #list Filter
    list_filter = ('category',)


class InvoiceAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created', 'customer', 'invoice_id',  'total_amount', 'vat_amount', 'get_grand_total', 'get_total_amount_paid']
    search_fields = ['customer', ]
    list_per_page = 400

class InvoiceItemAdmin(ImportExportModelAdmin):
    list_display = ['created', 'invoice', 'product', 'quantity', 'price',  'discount', 'total_discount',
     'total_amount', 'net_amount']
    list_per_page = 400


class InvoicePaymentAdmin(ImportExportModelAdmin):
    list_display = [ 'created', 'payment_session', 'payment_installment', 'employee', 'invoice', 'amount_paid', 'payment_id',]



admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(InvoicePayment, InvoicePaymentAdmin)






class CommissionEarnedForm(forms.ModelForm):
    class Meta:
        model = CommissionEarned
        fields = "__all__"
        exclude = ('slug',)

class OpeningDamageForm(forms.ModelForm):
    class Meta:
        model = OpeningDamage
        fields = "__all__"
        exclude = ('slug',)

class OpeningReturnForm(forms.ModelForm):
    class Meta:
        model = OpeningReturn
        fields = "__all__"
        exclude = ('slug',)

class InvoicePaymentForm(forms.ModelForm):
    class Meta:
        model = InvoicePayment
        fields = "__all__"
        exclude = ('slug',)

class OpeningBalanceForm(forms.ModelForm):
    class Meta:
        model = OpeningBalance
        fields = "__all__"
        exclude = ('slug',)

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = "__all__"
        exclude = ('slug',)


#--------------VIEWS-----------------#
def home(request):
    invoices = Invoice.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = invoices.count()
    active_customers = customers.filter(is_active=True).count()

    template_name = 'bakerycustomersinvoices/index.html'
    context = {'invoices':invoices, 'customers':customers,
                'active_customers':active_customers,
                'total_customers':total_customers,
                'total_orders':total_orders,
                }
    return render(request, template_name, context)


    def departments_view(request):
        departments = Department.objects.all()

        template_name = 'bakerycustomersinvoices/departments.html'
        context = {'departments':departments}
        return render(request, template_name, context)

    def categories_view(request):
        categories = Category.objects.all()

        template_name = 'bakerycustomersinvoices/categories.html'
        context = {'categories':categories}
        return render(request, template_name, context)


    def products_view(request):
        products = Product.objects.all()

        template_name = 'bakerycustomersinvoices/products.html'
        context = {'products':products}
        return render(request, template_name, context)

    def invoice_view(request):
        invoices = Invoice.objects.all().order_by('-created')
        #invoice_grand_total = list(invoices.aggregate(Sum('grand_total')).values())[0]

        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if start_date:
            invoices = invoices.filter(created__range=[start_date, end_date])
            #total_orders = list(invoices.filter(created__range=[start_date, end_date]).aggregate(Sum('amount')).values())[0]

        else:
            invoices = Invoice.objects.all().order_by('-created')
            #total_orders = list(invoices.aggregate(Sum('amount')).values())[0]

        template_name = 'bakerycustomersinvoices/invoices.html'
        context = {'invoices':invoices,

                    }
        return render(request, template_name, context)


    def InvoicePayment_view(request):
        invoice_payments = InvoicePayment.objects.all().order_by('-created')
        #invoice_grand_total = list(invoices.aggregate(Sum('grand_total')).values())[0]

        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if start_date:
            invoice_payments = invoice_payments.filter(created__range=[start_date, end_date])
            #total_orders = list(invoices.filter(created__range=[start_date, end_date]).aggregate(Sum('amount')).values())[0]

        else:
            invoices = InvoicePayment.objects.all().order_by('-created')
            #total_orders = list(invoices.aggregate(Sum('amount')).values())[0]

        template_name = 'bakerycustomersinvoices/invoice_payments.html'
        context = {'invoice_payments':invoice_payments,

                    }
        return render(request, template_name, context)


    def invoice_details_print(request, invoice_id):
        invoice = get_object_or_404(Invoice, pk=invoice_id)

        items = invoice.invoiceitem_set.all()
        items_total = list(items.aggregate(Sum('net_amount')).values())[0]

        invoice_payment = invoice.invoicepayment_set.all()
        total_invoice_payment = list(invoice_payment.aggregate(Sum('amount_paid')).values())[0]

        payment_installment_count = invoice_payment.count()


        balance_due = items_total - total_invoice_payment
        if balance_due > 0:
            balance_due = balance_due
        else:
            balance_due = 0

        template_name = 'bakerycustomersinvoices/invoice-template.html'
        context = {
                    'invoice':invoice,
                    'items_total':items_total,

                    'total_invoice_payment':total_invoice_payment,
                    'payment_installment_count':payment_installment_count,

                    'balance_due':balance_due,


                    }
        return render(request, template_name, context)



    def customer_details(request, slug):
        customer = Customer.objects.get(slug=slug)
        opening_balance = customer.openingbalance_set.all()
        order = customer.order_set.all()
        payment = customer.payment_set.all()
        opening_returns = customer.openingreturn_set.all()
        opening_damage = customer.openingdamage_set.all()
        cus_commission = customer.commissionearned_set.all()

        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if start_date:
            orders = order.filter(created__range=[start_date, end_date])
            total_orders_amount = list(order.filter(created__range=[start_date, end_date]).aggregate(Sum('amount')).values())[0]

        else:
            orders = order
            total_orders_amount = list(order.aggregate(Sum('amount')).values())[0]

        total_opening_balance = list(opening_balance.aggregate(Sum('amount')).values())[0]
        total_payments_amount = list(payment.aggregate(Sum('amount')).values())[0]
        total_opening_returns = list(opening_returns.aggregate(Sum('amount')).values())[0]
        total_damages = list(opening_damage.aggregate(Sum('amount')).values())[0]
        total_commission_earned = list(cus_commission.aggregate(Sum('amount')).values())[0]
        total_orders_amount1 = list(order.aggregate(Sum('amount')).values())[0]

        #account_balance = total_opening_balance + total_orders_amount


        template_name = 'bakerycustomersinvoices/invoice-template.html'
        context = {'customer':customer,

                    'orders':orders,
                    'total_orders_amount':total_orders_amount,
                    #'payments':payments,
                    #'returns':opening_returns,
                    #'damages':opening_damage,


                    'opening_balance':opening_balance,
                    'total_opening_balance':total_opening_balance,
                    'total_payments_amount':total_payments_amount,

                    'total_opening_returns':total_opening_returns,
                    'total_damages':total_damages,
                    'total_orders_amount1':total_orders_amount1,

                    #'account_balance':account_balance,
                    #'total_commission_earned':total_commission_earned


                    }
        return render(request, template_name, context)

    class add_customer(SuccessMessageMixin, CreateView):
        model = Customer
        template_name = 'bakerycustomersinvoices/forms/add_customer.html'
        fields = '__all__'
        exclude = ('slug',)
        success_url = reverse_lazy('bakerycustomersinvoices:home')
        success_message = 'Customer Accounts Successfully Created !!!'

    class edit_customer(SuccessMessageMixin,UpdateView):
        model = Customer
        template_name = 'bakerycustomersinvoices/forms/edit_customer.html'
        fields = '__all__'
        exclude = ('slug',)
        success_url = reverse_lazy('bakerycustomersinvoices:home')
        success_message = 'Customer Accounts Successfully Edited !!!'

    def opening_balance_view(request):

        opening_balance = OpeningBalance.objects.all().order_by('-created')

        template_name = 'bakerycustomersinvoices/opening_balance.html'
        context = {'opening_balances':opening_balance}
        return render(request, template_name, context)



    def add_opening_balance(request):
        form = OpeningBalanceForm(request.POST or None)

        if form.is_valid():
            opening_balance = form.save(commit=False)
            opening_balance.save()
            opening_balance.customer.account_number = opening_balance.customer.account_number
            # adds client deposit to balance
            opening_balance.customer.account_balance += opening_balance.amount
            opening_balance.customer.save()
            messages.success(
                request, 'Client Have successfully purchased for  {} cfa.'.format(opening_balance.amount))
            return redirect('bakerycustomersinvoices:home')
        context = {'form': form}
        return render(request, 'bakerycustomersinvoices/forms/add_opening_bal.html', context)



    class edit_opening_balance(SuccessMessageMixin, UpdateView):
        model = OpeningBalance
        template_name = 'bakerycustomersinvoices/forms/edit_opening_bal.html'
        fields = '__all__'
        exclude = ('slug',)
        success_url = reverse_lazy('task:task-home')
        success_message = 'Opening Balance Edited successfully !!!'


    def add_order_view(request):
        form = OrderForm(request.POST or None)

        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            order.customer.account_number = order.customer.account_number
            # adds client deposit to balance
            order.customer.account_balance += order.amount
            order.customer.save()
            messages.success(
                request, 'Order for  {} cfa is successful.'.format(order.amount))
            return redirect('bakerycustomersinvoices:home')
        context = {'form': form}
        return render(request, 'bakerycustomersinvoices/forms/add_order.html', context)

    class edit_order(SuccessMessageMixin, UpdateView):
        model = Invoice
        template_name = 'bakerycustomersinvoices/forms/edit_order.html'
        fields = '__all__'
        success_url = reverse_lazy('bakerycustomersinvoices:order')
        success_message = 'Order Edited successfully !!!'

    def payments_view(request):

        payments = Payment.objects.all().order_by('-created')
        total_payments = list(payments.aggregate(Sum('amount')).values())[0]

        template_name = 'bakerycustomersinvoices/payments.html'
        context = {'payments':payments, 'total_payments':total_payments}
        return render(request, template_name, context)


    class add_payment_view(SuccessMessageMixin, CreateView):
        model = InvoicePayment
        template_name = 'bakerycustomersinvoices/forms/add_payment.html'
        fields = '__all__'
        #exclude = ('slug',)
        success_url = reverse_lazy('bakerycustomersinvoices:payments')
        success_message = 'Payment Transaction successful'

    class edit_payment(SuccessMessageMixin, UpdateView):
        model = InvoicePayment
        template_name = 'bakerycustomersinvoices/forms/edit_payment.html'
        fields = '__all__'
        #exclude = ('slug',)
        success_url = reverse_lazy('bakerycustomersinvoices:payments')
        success_message = 'Payment Transaction successful'

    def damages_view(request):
        damages= OpeningDamage.objects.all().order_by('-created')
        total_damages = list(damages.aggregate(Sum('amount')).values())[0]

        template_name = 'bakerycustomersinvoices/damages.html'
        context = {'damages':damages, 'total_damages':total_damages }
        return render(request, template_name, context)


    class add_damage_view(SuccessMessageMixin, CreateView):
        model = OpeningDamage
        template_name = 'bakerycustomersinvoices/forms/add_damages.html'
        fields = '__all__'
        #exclude = ('slug',)
        success_url = reverse_lazy('bakerycustomersinvoices:damages')
        success_message = 'Damage Transaction successful'

    class edit_damages(SuccessMessageMixin, UpdateView):
        model = OpeningDamage
        template_name = 'bakerycustomersinvoices/forms/edit_damages.html'
        fields = '__all__'
        #exclude = ('slug',)
        success_url = reverse_lazy('bakerycustomersinvoices:damages')
        success_message = 'Damage Transaction successful'


    def returns_view(request):

        returns = OpeningReturn.objects.all().order_by('-created')
        total_returns = list(returns.aggregate(Sum('amount')).values())[0]

        template_name = 'bakerycustomersinvoices/returns.html'
        context = {'returns':returns, 'total_returns':total_returns}
        return render(request, template_name, context)


    class add_return_view(SuccessMessageMixin, CreateView):
        model = OpeningReturn
        template_name = 'bakerycustomersinvoices/forms/add_returns.html'
        fields = '__all__'
        #exclude = ('slug',)
        success_url = reverse_lazy('bakerycustomersinvoices:returns')
        success_message = 'Returns Transaction successful'

    class edit_returns(SuccessMessageMixin, UpdateView):
        model = OpeningReturn
        template_name = 'bakerycustomersinvoices/forms/edit_returns.html'
        fields = '__all__'
        #exclude = ('slug',)
        success_url = reverse_lazy('bakerycustomersinvoices:returns')
        success_message = 'Returns Transaction successful'

    def commissionearned_view(request):

        commission_earned = CommissionEarned.objects.all().order_by('-created')
        total_commission = list(commission_earned.aggregate(Sum('amount')).values())[0]

        template_name = 'bakerycustomersinvoices/commission.html'
        context = {'commission_earneds':commission_earned,
                    'total_commission':total_commission}
        return render(request, template_name, context)

    class add_commission_view(SuccessMessageMixin, CreateView):
        model = CommissionEarned
        template_name = 'bakerycustomersinvoices/forms/add_commission.html'
        fields = '__all__'
        #exclude = ('slug',)
        success_url = reverse_lazy('bakerycustomersinvoices:commission')
        success_message = 'Commission Transaction successful'


    class edit_commission(SuccessMessageMixin, UpdateView):

        model = CommissionEarned
        template_name = 'bakerycustomersinvoices/forms/add_commission.html'
        fields = '__all__'
        #exclude = ('slug',)
        success_url = reverse_lazy('bakerycustomersinvoices:commission')
        success_message = 'Commission Transaction successful'

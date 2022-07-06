from django.db import models

# Create your models here.
from django.db import models
#from . utility import code_format
import datetime
from django.utils.timezone import now
from django.template.defaultfilters import slugify
import uuid
import shortuuid
import random
from django.urls import reverse


# Create your models here.
class Employee(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    LEVELOFEDUCATION = (
        ('FSLC', 'FSLC'),
        ('Ordinary Level', 'Ordinary Level'),
        ('Advanced Level', 'Advanced Level'),
        ('Bachelor Degree', 'Bachelor Degree'),
        ('Master Degree', 'Master Degree'),
        ('MBA', 'MBA'),
        ('PHD', 'PHD'),
    )

    RELIGION =  (
        ('Christian', 'Christian'),
        ('Muslim', 'Muslim'),
        ('Others', 'Others'),
    )

    EMERGENCYRELATIONSHIP =  (
        ('FATHER', 'FATHER'),
        ('MOTHER', 'MOTHER'),
        ('UNCLE', 'UNCLE'),
        ('AUNTY', 'AUNTY'),
        ('BROTHER', 'BROTHER'),
        ('SISTER', 'SISTER'),
        ('HUSBAND', 'HUSBAND'),
        ('WIFE', 'WIFE'),
        ('BOY FRIEND', 'BOY FRIEND'),
        ('GIRL FRIEND', 'GIRL FRIEND'),
        ('OTHERS', 'OTHERS'),
    )

    EMPLOYMENT_STATUS =  (
        ('ACTIVE', 'ACTIVE'),
        ('ON LEAVE', 'ON LEAVE'),
        ('SUSPENDED', 'SUSPENDED'),
        ('DIMISSED', 'DIMISSED'),
    )

    EMPLOYMENT_TYPE =  (
        ('PART TIME', 'PART TIME'),
        ('FULL TIME', 'FULL TIME'),
        ('CONTRACT', 'CONTRACT'),
    )


    # PERSONAL DATA
    #user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    #image = models.FileField(('Profile Image'),upload_to='profiles',default='default.png',blank=True,null=True,help_text='upload image size less than 2.0MB')#work on path username-date/image
    firstname = models.CharField(('First Name'),max_length=1250,null=False,blank=False)
    lastname = models.CharField(('Last Name'),max_length=1250,null=False,blank=False)
    middle_name = models.CharField(('Middle Name (optional)'),max_length=125,null=True,blank=True)
    id_card_number = models.CharField(('ID Card Number'),max_length=30,null=True,blank=True)
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True)
    slug = models.SlugField(max_length=1000, unique=True, blank=True, null=True)

    # Demographics
    gender = models.CharField(('Gender'),max_length=255,blank=False, choices=GENDER,default='')
    birthday = models.DateField(('Date of Birth (YY/MM/DD)'),blank=False,null=False, default='')
    birth_place = models.CharField(('Place of Birth (optional)'), max_length=255,blank=True,null=True)
    tribe = models.CharField(('Tribe (optional)'), max_length=255,blank=True,null=True)
    religion = models.CharField(('Religion (optional)'), max_length=255,default=None,blank=True,null=True, choices=RELIGION)
    nationality = models.CharField(('Nationality (optional)'), max_length=255,default=None,blank=True,null=True)
    ssnitnumber = models.CharField(('Social Insurance Number'),max_length=30,null=True,blank=True)

    # Contact
    tel = models.CharField( max_length=255, null = True, blank=True, verbose_name='Phone Number 1 ' )
    tel2 = models.CharField( max_length=255 ,null = True, blank=True, verbose_name='Phone Number 2 ')
    email = models.CharField(('Email (optional)'), max_length=255,default=None,blank=True,null=True)


    # Address
    current_town = models.CharField(('Hometown (optional)'), max_length=255, default=None, blank=True, null=True)
    region = models.CharField(('Region (optional)'), max_length=255, default=None, blank=True, null=True)
    quarter = models.CharField(('Current Quarter'),max_length=125, default=None, null=False, blank=False)
    address = models.TextField(('Address'),help_text='address of current residence', max_length=125, null=True, blank=True)

    # Education Level
    education = models.TextField(('Level of Education'),max_length=125,null=True,blank=True, choices=LEVELOFEDUCATION)

    # Previous Working Condions
    lastwork = models.CharField(('Last Place of Work'),help_text='where was the last place you worked ?',max_length=125,null=True,blank=True)
    previous_employer = models.CharField(('Previous Employer'),help_text='Previous Employer ?',max_length=255,null=True,blank=True)
    position = models.CharField(('Position Held'),help_text='what position where you in your last place of work ?',max_length=255,null=True,blank=True)
    location =  models.CharField(('Location last-work'),help_text='Location last-work ?',max_length=255,null=True,blank=True)

    #type_of_work = models.CharField(('Type of Business'),help_text='Type of Business?',max_length=255,null=True,blank=True)
    #other_experiences =  models.CharField(('Other Experiences'),help_text='Other Experiences ?',max_length=255,null=True,blank=True)
    #reasons_for_termination =  models.CharField(('Reasons for Termination'),help_text='Why you left ?',max_length=255,null=True,blank=True)


    # COMPANY DATA
    #department =  models.ForeignKey(SubDepartment, null=True, on_delete=models.SET_NULL)
    #role =  models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
    #employmenttype = models.CharField(('Employment Type'),max_length=30,null=True,blank=True, choices =EMPLOYMENT_TYPE)
    #employeeid = models.CharField(('Employee ID Number'), max_length = 10, blank=True, editable=False, unique=True, default=uuid.uuid4)
    #employment_status = models.CharField(('Employement Status'),max_length=30,null=True,blank=True, choices= EMPLOYMENT_STATUS)
    #startdate = models.DateField(('Employement Date'),help_text='date of employement',blank=True,null=True)
    #enddate = models.DateField(('Termination Date'),help_text='date of employement',blank=True,null=True)


    #total_salary = models.IntegerField(default=0)
    #base_salary = models.IntegerField(('Base Salary'),help_text='Total Salary - sum of all allowance',default=0, blank=True,null=True)
    #housing_allowance = models.IntegerField(('Housing Allowance'),help_text='15% of Total Salary', default=0, blank=True,null=True)
    #feeding_allowance = models.IntegerField(('Feeding Allowance'),help_text='10% of Total Salary',  default=0, blank=True,null=True)
    #light_allowance = models.IntegerField(('Electricity Allowance'),help_text='4% of Total Salary',  default=0, blank=True,null=True)
    #water_allowance = models.IntegerField(('WaterBill Allowance'),help_text='2% of Total Salary',  default=0, blank=True,null=True)
    #transport_allowance = models.IntegerField(('WaterBill Allowance'),help_text='10% of Total Salary',  default=0, blank=True,null=True)

    # Emergency CONTRACT 1
    #fullname1 = models.CharField(('Fullname'),help_text='who should we contact ?', max_length=255,null=True,blank=False)
    #tel1 = models.CharField(max_length=255, null = False, blank=False,default= '+237', verbose_name='Emergency Contact Tel ', help_text= 'Phone Number')
    #relationship1 = models.CharField(('Relationship 1'),help_text='who should we contact ?',max_length=255,null=True,blank=False, choices=EMERGENCYRELATIONSHIP)
    #place_of_residence1 = models.CharField(('Place of Residence'),max_length= 255,null=True,blank=False)

        # Emergency CONTRACT 2
    #fullname2 = models.CharField(('Fullname 2'),help_text='who should we contact ?',max_length=255,null=True,blank=False)
    #tel3 = models.CharField(max_length=255, null = False, blank=False,default= '+237', verbose_name='Emergency Contact Tel ', help_text= 'Phone Number')
    #relationship2 = models.CharField(('Relationship 2'),help_text='who should we contact ?',max_length=255,null=True,blank=False, choices=EMERGENCYRELATIONSHIP)
    #place_of_residence2 = models.CharField(('Place of Residence'),max_length= 255,null=True,blank=False)

    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True,null=True)

    class Meta:
        verbose_name = ('Employee')#
        verbose_name_plural = ('Employees')
        #ordering = ['-created']

    #def __str__(self):
        #return self.firstname

    #def get_absolute_url(self):
        #return reverse('payroll:employee-detail', args=[self.slug])

    #@property
    #def get_full_name(self):
        #fullname = ''
        #firstname = self.firstname
        #lastname = self.lastname
        #middlename = self.middle_name

       # if (firstname and lastname) or othername is None:
            #fullname = firstname +' '+ lastname +' '+middlename
           # return fullname
        #elif othername:
            #fullname = firstname + ' '+ lastname
            #return fullname
        #return

    #@property
    #def get_age(self):
        #current_year = datetime.date.today().year
        #dateofbirth_year = self.birthday.year
        #if dateofbirth_year:
            #return current_year - dateofbirth_year
        #return

    #@property
    #def get_housing_allowance(self):
        #if self.total_salary:
            #return (15/100) * self.total_salary
            #return

    #@property
    #def get_feeding_allowance(self):
        #if self.total_salary:
            #return (10/100) * self.total_salary
            #return

    #@property
    #def get_transport_allowance(self):
        #if self.total_salary:
            #return (10/100) * self.total_salary
            #return

    #@property
    #def get_light_allowance(self):
        #if self.total_salary:
            #return (4/100) * self.total_salary
            #return

    #@property
    #def get_water_allowance(self):
        #if self.total_salary:
            #return (2/100) * self.total_salary
            #return


    def save(self, *args, **kwargs):
            self.slug = slugify(self.firstname)
            #self.housing_allowance = self.get_housing_allowance
            #self.transport_allowance = self.get_transport_allowance
            #self.feeding_allowance = self.get_feeding_allowance
            #self.light_allowance = self.get_light_allowance
            #self.water_allowance = self.get_water_allowance
            #self.base_salary = self.total_salary -  (self.housing_allowance + self.transport_allowance + self.feeding_allowance + self.light_allowance + self.water_allowance)
            super(Employee, self).save(*args, **kwargs)


'''
def increment_invoice_number():
    last_invoice = Salaries.objects.all().order_by('id').last()
    today = datetime.date.today()
    today_string = today.strftime("%Y-%m-%d")

    if not last_invoice:
         return today_string + "-" + 'SAL0001'

    transaction_id = last_invoice.transaction_id
    invoice_int = int(transaction_id.split('SAL000')[-1])
    new_invoice_int = invoice_int + 1

    new_transaction_id = today_string + "-" + 'SAL000'  + str(new_invoice_int)
    return new_transaction_id



class Salaries(models.Model):
    PAY_TYPE = (
    ('Monthly', 'Monthly'),
    ('Weekly', 'Weekly'),
    ('Daily', 'Daily'),
    )

    PAYMENT_MEANS = (
    ('Cash', 'Cash'),
    ('Bank', 'Bank'),
    ('Cheque', 'Cheque'),
    ('Mobile Money', 'Mobile Money'),
    )

    created = models.DateField(default=now)
    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    payment_type =  models.CharField(max_length=100, default='', choices=PAY_TYPE)
    payment_means =  models.CharField(max_length=100, default='', choices=PAYMENT_MEANS)

    transaction_id = models.CharField(max_length = 500,default=uuid.uuid4(), null = True, blank = True)
    #max_length = 10, blank=True, editable=False, unique=True, default=uuid.uuid4

    # Earnings
    total_salary = models.IntegerField(default=0)

    base_salary = models.IntegerField(('Base Salary'),help_text='Total Salary - sum of all allowance',default=0, blank=True,null=True)
    housing_allowance = models.IntegerField(('Housing Allowance'),help_text='15% of Total Salary', default=0, blank=True,null=True)
    feeding_allowance = models.IntegerField(('Feeding Allowance'),help_text='10% of Total Salary',  default=0, blank=True,null=True)
    light_allowance = models.IntegerField(('Electricity Allowance'),help_text='4% of Total Salary',  default=0, blank=True,null=True)
    water_allowance = models.IntegerField(('WaterBill Allowance'),help_text='2% of Total Salary',  default=0, blank=True,null=True)
    transport_allowance = models.IntegerField(('WaterBill Allowance'),help_text='10% of Total Salary',  default=0, blank=True,null=True)

    overtime = models.IntegerField(default=0,blank=True,null=True)
    commission_and_bonus = models.IntegerField(default=0,blank=True,null=True)
    expenses = models.IntegerField(default=0,blank=True,null=True)

    total_earnings = models.IntegerField(default=0,blank=True,null=True)

    # Deductions
    income_tax = models.IntegerField(default=0,blank=True,null=True)
    national_social_insurance = models.IntegerField(default=0,blank=True,null=True)
    other_dedutions = models.IntegerField(default=0,blank=True,null=True)
    reasons_for_deductions = models.TextField(max_length=1000,blank=True,null=True)

    total_deductions = models.IntegerField(default=0,blank=True,null=True)

    total_expected_amount_to_paid = models.IntegerField(default=0,blank=True,null=True)
    total_amount_paid = models.IntegerField(default=0,blank=True,null=True)

    arrears = models.IntegerField(default=0,blank=True,null=True)

    def __str__(self):
        return str(self.employee.get_full_name)

    class Meta:
        ordering = ['-created']

    class Meta:
        verbose_name = ('Salary')
        verbose_name_plural = ('Salaries')
        ordering = ['-created']


    @property
    def get_total_earnings(self):
        virtual_amount = 0
        if self.base_salary:
            return self.total_salary + self.overtime + self.commission_and_bonus + self.expenses
        else:
            return virtual_amount

    @property
    def get_total_dedutions(self):
        virtual_amount = 0
        if self.base_salary:
            return self.income_tax + self.national_social_insurance + self.other_dedutions
        else:
            return virtual_amount

    @property
    def get_expected_amount_to_paid(self):
        return self.total_earnings - self.total_deductions
        return

    @property
    def get_arrears(self):
        if self.total_expected_amount_to_paid:
            return self.total_expected_amount_to_paid - self.total_amount_paid


    def save(self, *args, **kwargs):
        self.base_salary  = self.employee.base_salary
        self.housing_allowance = self.employee.housing_allowance
        self.feeding_allowance = self.employee.feeding_allowance
        self.light_allowance = self.employee.light_allowance
        self.water_allowance = self.employee.water_allowance
        self.transport_allowance = self.employee.transport_allowance

        self.total_salary = self.employee.total_salary

        self.total_earnings = self.get_total_earnings
        self.total_deductions = self.get_total_dedutions

        self.total_expected_amount_to_paid = self.get_expected_amount_to_paid
        self.arrears = self.get_arrears
        super(Salaries, self).save(*args, **kwargs)



'''
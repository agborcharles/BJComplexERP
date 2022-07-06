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
    firstname = models.CharField(('First Name'),max_length=250,null=False,blank=False)
    lastname = models.CharField(('Last Name'),max_length=250,null=False,blank=False)
    middle_name = models.CharField(('Middle Name (optional)'),max_length=125,null=True,blank=True)
    fullname = models.CharField(('Full Name (Leave Blank)'),max_length=125,null=True,blank=True, default='')
    id_card_number = models.CharField(('ID Card Number'),max_length=30,null=True,blank=True)
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    # Demographics
    gender = models.CharField(max_length=100, blank=True, null=True, choices=GENDER, default='')
    birthday = models.DateField(('Date of Birth (YY/MM/DD)'),blank=False,null=False, default='')
    age = models.IntegerField(('Age'),null=True, blank=True, default=0,)
    birth_place = models.CharField(('Place of Birth (optional)'), max_length=255,blank=True,null=True)
    tribe = models.CharField(('Tribe (optional)'), max_length=255,blank=True,null=True)
    religion = models.CharField(('Religion (optional)'), max_length=255,default=None,blank=True,null=True, choices=RELIGION)
    nationality = models.CharField(('Nationality (optional)'), max_length=255,default=None,blank=True,null=True)
    ssnitnumber = models.CharField(('Social Insurance Number'),max_length=30,null=True,blank=True)

    # Contact
    tel = models.CharField( max_length=255, null = True, blank=True, verbose_name='Phone Number 1 ' )
    tel2 = models.CharField( max_length=255 ,null = True, blank=True, verbose_name='Phone Number 2 ')
    email = models.CharField(('Email (optional)'), max_length=255,default=None,blank=True,null=True)

    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True,null=True)

    def __str__(self):
        return str(self.firstname)

    class Meta:
        verbose_name = ('Employee')
        verbose_name_plural = ('Employees')

#------------------------------- Property Calculations ---------------------------------#
    @property
    def get_full_name(self):
        fullname = ''
        firstname = self.firstname
        lastname = self.lastname
        middlename = self.middle_name
    
    @property
    def get_age(self):
        current_year = datetime.date.today().year
        dateofbirth_year = self.birthday.year
        if dateofbirth_year:
            return current_year - dateofbirth_year
        return


    def save(self, *args, **kwargs):
            self.slug = slugify(self.firstname + ' ' + self.lastname + ' ' + self.id_card_number)
            self.fullname = (self.firstname.capitalize()) + ' ' + (self.lastname.capitalize())
            self.age = self.get_age
            super(Employee, self).save(*args, **kwargs)



from django.db import models
#from django.urls import reverse
import datetime
#from django.db.models import Q
#from django.conf import settings
from django.utils.datetime_safe import date
#from django.contrib.auth.models import User, AbstractUser
#from django.db.models.signals import post_save
#from django.dispatch import receiver

'''
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField("Mobile", max_length=10)
    email = models.EmailField("Email", max_length=40)
    city = models.CharField("City", max_length=30)
    pin = models.CharField("Pincode", max_length=6)
    main_company_name = models.CharField("Main Company Name", max_length=50)
    company_code = models.CharField("Company Code", max_length=8)
    module = models.CharField("Module", max_length=1)
    start_date = models.DateField("Start Date", default="9999-12-31")
    end_date = models.DateField("End Date", default="9999-12-31")
    select = models.CharField("Company", max_length=8, default='-')


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

'''

'''
class CompMstr(models.Model):
    company_code = models.CharField("Company Code", primary_key=True, max_length=8)
    comp_name = models.CharField("Company Name", max_length=50)
    company_type = models.CharField("Company Type", max_length=9)
    address_1 = models.CharField("Address 1", max_length=50, default='-')
    address_2 = models.CharField("Address 2", max_length=50, default='-')
    city = models.CharField("City", max_length=30)
    pin = models.CharField("Pincode", max_length=6, default='-')
    state_code = models.CharField("State Code", max_length=2)
    phone = models.CharField("Phone", max_length=11)
    mobile = models.CharField("Mobile", max_length=10)
    gst_no = models.CharField("GST Number", max_length=15)
    pan_no = models.CharField("PAN Number", max_length=10)
    bank_name = models.CharField("Bank Name", max_length=50)
    bank_branch = models.CharField("Bank Branch", max_length=50)
    ac_no = models.CharField("Account Number", max_length=20)
    ifsc_code = models.CharField("IFSC Code", max_length=11)
    jurisdiction = models.CharField("Jurisdiction", max_length=15)
    interest_rate = models.DecimalField("Interest Rate", max_digits=4, decimal_places=2)
    invoice_footer = models.TextField("Invoice Footer", max_length=500, default='-')
    quotation_footer = models.TextField("Quotation Footer", max_length=500, default='-')
    year_start = models.DateField("Financial Year Start")
    year_end = models.DateField("Financial Year End")
    work_start = models.DateField("Work Year Start")
    work_end = models.DateField("Work Year End")
    credit_days = models.IntegerField("Credit Days")

'''


class AcMstr(models.Model):
    code = models.CharField("Code", max_length=8)
    name = models.CharField("Full name", max_length=50)
    address_1 = models.CharField("Address line 1", max_length=50, default='-')
    address_2 = models.CharField("Address line 2", max_length=50, default='-')
    city = models.CharField("City", max_length=15, null=True)
    pin = models.CharField("ZIP / Postal code", max_length=6, default='-')
    state_code = models.CharField("State Code", max_length=2, default='-')
    gst_no = models.CharField("GST Number", max_length=15, default='-')
    pan_aadhar_no = models.CharField("PAN / Aadhar Number", max_length=16, default='-')
    bp_type = models.CharField("Business Partner Type", max_length=10)
    group_code = models.CharField("Business Group", max_length=3, default='-', blank=True)
    #company_code = models.ForeignKey(CompMstr, on_delete=models.CASCADE)
    bsgrp = models.IntegerField("Balance Sheet Group", default=0)
    bssubgrp = models.IntegerField("Balance Sheet Sub-Group", default=0)
    opbal = models.DecimalField("Opening Balance", max_digits=14, decimal_places=2, default=0, blank=True)
    clbal = models.DecimalField("Closing Balance", max_digits=14, decimal_places=2, default=0, blank=True)
    temp_bal = models.DecimalField("Temp. Balance", max_digits=14, decimal_places=2, default=0, blank=True)
    user = models.CharField("User", max_length=20)
    upd_time = models.DateTimeField("Update Date and Time", auto_now=True)
    share_dep = models.DecimalField("Share-Dep %", max_digits=5, decimal_places=2, default=0, blank=True)
    email = models.CharField("Email", max_length=35)
    phone = models.CharField("Phone", max_length=25)
    pwd = models.CharField("Password", max_length=15)




class ShowMstr(models.Model):
    #code = models.ForeignKey(AcMstr, on_delete=models.CASCADE)
    show_code = models.CharField("Show Code", max_length=8)
    show_name = models.CharField("Show Name", max_length=30)
    start_date = models.DateField("Start Date", default=date.today)




class ItemMstr(models.Model):
    it_code = models.CharField("Item Code", max_length=8)
    it_name = models.CharField("Item Name", max_length=20)
    location = models.CharField("Location", max_length=25)
    sac_code = models.IntegerField("SAC Code", default=998363)
    gst = models.DecimalField("GST", max_digits=2, decimal_places=2, default=5)



'''
class SizeMstr(models.Model):
    size = models.CharField("Size", max_length=10)

'''


class TypeMstr(models.Model):
    type = models.CharField("Type", max_length=8)
    type_name = models.CharField("Type Name", max_length=40)

    def __str__(self):
        return self.type,self.type_name

'''
class ADlocMstr(models.Model):
    loc_code = models.CharField("Location Code", max_length=8)
    loc_name = models.CharField("Location Name", max_length=15)

'''

'''
class Transaction(models.Model):
    vr_no = models.IntegerField("Voucher Number")
    tr_date = models.DateField("Transaction Date")
    it_code = models.ForeignKey(ItemMstr, on_delete=models.CASCADE)
    size = models.ForeignKey(SizeMstr, on_delete=models.CASCADE)
    type = models.ForeignKey(TypeMstr, on_delete=models.CASCADE)
    remark = models.CharField("Remark", max_length=25)
    code = models.ForeignKey(AcMstr, on_delete=models.CASCADE)
    show_code = models.ForeignKey(ShowMstr, on_delete=models.CASCADE)
    start_date = models.DateField("Start Date", default=date.today)
    discount = models.DecimalField("Discount", max_digits=5, decimal_places=2, default=0)
    plan_type = models.CharField("Plan Type", max_length=15)

'''
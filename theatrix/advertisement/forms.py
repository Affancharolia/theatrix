#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Submit
from django import forms
from .models import TypeMstr, ItemMstr, AcMstr, ShowMstr

# ItemMaster
class ItemForm(forms.Form):
	model = ItemMstr

	it_code = forms.CharField(label='Item Code', max_length=8, widget=forms.TextInput(
		attrs={'style': 'text-transform:uppercase;', 'autofocus': True}))
	it_name = forms.CharField(label='Item Name', max_length=20)
	location = forms.CharField(label='Location', max_length=25)
	sac_code = forms.IntegerField(label='SAC Code')
	gst = forms.DecimalField(label='GST', max_digits=2, decimal_places=2)

	class Meta:
		model = ItemMstr
		fields = ('it_code', 'it_name', 'location', 'sac_code', 'gst')

# TypeMaster
class TypeForm(forms.Form):
	model = TypeMstr

	type = forms.CharField(label='Type', max_length=8, widget=forms.TextInput(
		attrs={'style': 'text-transform:uppercase;', 'autofocus': True}))
	type_name = forms.CharField(label='Type Name', max_length=40)

	class Meta:
		model = TypeMstr
		fields = ('type', 'type_name')

#TypeMaster Update
class TypeUpdateForm(forms.Form):
	type_name = forms.CharField(label='Type Name', max_length=40)

	class Meta:
		class Meta:
			model = TypeMstr
			fields = ('type_name')


# AccountMaster
class AccountForm(forms.Form):
	model = AcMstr

	code = forms.CharField(label='Code', max_length=8, widget=forms.TextInput(
		attrs={'style': 'text-transform:uppercase;', 'autofocus': True}))
	name = forms.CharField(label='Full Name', max_length=50)
	address_1 = forms.CharField(label='Address Line 1', max_length=50)
	address_2 = forms.CharField(label='Address Line 2', max_length=50)
	city = forms.CharField(label='City', max_length=15)
	pin = forms.CharField(label='ZIP / Postal code', max_length=6, widget=forms.TextInput(
		attrs={'style': 'text-transform:uppercase;', 'autofocus': True}))
	state_code = forms.CharField(label='State Code', max_length=2, widget=forms.TextInput(
		attrs={'style': 'text-transform:uppercase;', 'autofocus': True}))
	gst_no = forms.CharField(label='GST Number', max_length=15)
	pan_aadhar_no = forms.CharField(label='PAN / Aadhar Number', max_length=16)
	bp_type = forms.CharField(label='Business Partner Type', max_length=10)
	group_code = forms.CharField(label='Business Group', max_length=3,widget=forms.TextInput(
		attrs={'style': 'text-transform:uppercase;', 'autofocus': True}))
	bsgrp = forms.IntegerField(label='Balance Sheet Group')
	bssubgrp = forms.IntegerField(label='Balance Sheet Sub-Group')
	opbal = forms.DecimalField(label='Opening Balance', max_digits=14, decimal_places=2)
	clbal = forms.DecimalField(label='Closing Balance', max_digits=14, decimal_places=2)
	temp_bal = forms.DecimalField(label='Temp. Balance', max_digits=14, decimal_places=2)
	user = forms.CharField(label='User', max_length=20)
	upd_time = forms.DateTimeField(label='Update Date and Time')
	share_dep = forms.DecimalField(label='Share-Dep %', max_digits=5, decimal_places=2)
	email = forms.CharField(label='Email', max_length=35)
	phone = forms.CharField(label='Phone', max_length=25)
	pwd = forms.CharField(label='Password', max_length=15)

# ShowMaster
class ShowForm(forms.Form):
	model = ShowMstr

	show_code = forms.CharField(label='Show Code', max_length=8, widget=forms.TextInput(
		attrs={'style': 'text-transform:uppercase;', 'autofocus': True}))
	show_name = forms.CharField(label='Show Name', max_length=30)
	start_date = forms.DateField(label='Start Date')


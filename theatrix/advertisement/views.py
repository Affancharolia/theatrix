from django.shortcuts import render, get_object_or_404
'''from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm'''
from .forms import TypeForm, ItemForm, AccountForm, ShowForm, TypeUpdateForm
from .models import TypeMstr, ItemMstr, AcMstr, ShowMstr
from django.urls import reverse_lazy

#from .forms import ItemForm, ItemUpdateForm
# Create your views here.


def items(request):

    all_items = ItemMstr.objects.all()
    message1 = ""
    message2 = ""
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            it_code = form.cleaned_data.get('it_code').upper()
            if ItemMstr.objects.filter(it_code=it_code).exists():
                message1 = "Item Code already exists"
                return render(request, 'items.html',
                              {"message1": message1, "message2": message2,
                               "form": form,
                               "view": all_items})
            it_name = form.cleaned_data.get('it_name')
            if ItemMstr.objects.filter(it_name=it_name).exists():
                message2 = "Item Name already exists"
                return render(request, 'items.html',
                              {"message1": message1, "message2": message2,
                                "form": form,
                               "view": all_items})
            location = form.cleaned_data['location']
            sac_code = form.cleaned_data['sac_code']
            gst = form.cleaned_data['gst']
            item_data = ItemMstr(it_code = it_code, it_name = it_name, location = location, sac_code = sac_code, gst = gst)
            item_data.save()
            form = ItemForm()

    else:
        form = ItemForm()


    return render(request, 'items.html', {'form': form, 'view': all_items})

def itemsview(request):
    all_items = ItemMstr.objects.all()
    #item_filter = ItemFilter(request.GET, queryset=all_items)

    return render(request, 'itemmaster.html', {"view": all_items})



def types(request):

    all_items = TypeMstr.objects.all()
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():

            type = form.cleaned_data['type']
            type_name = form.cleaned_data['type_name']
            type_data = TypeMstr(type=type, type_name=type_name)
            type_data.save()
            all_items = TypeMstr.objects.all()
            form = TypeForm()

    else:
        form = TypeForm()
    return render(request, 'types.html', {'form': form, 'view': all_items})

def typesview(request):
    all_items = TypeMstr.objects.all()
    #item_filter = ItemFilter(request.GET, queryset=all_items)

    return render(request, 'typemaster.html', {"view": all_items})

def typedeleteview(request, type):
    obj = get_object_or_404(TypeMstr, type=type)
    if request.method == 'POST':
        obj.delete()
    context = {
        'object': obj
    }
    success_url = reverse_lazy('typesview')
    return render(request, 'delete.html', context)

def typeupdateview(request, type):
    item = TypeMstr.objects.filter(type=type)
    item.refresh_from_db()
    form = TypeUpdateForm()
    success_url = reverse_lazy('typesview')
    return render(request, 'typesupdate.html', {'form': form})



def accounts(request):

    all_items = AcMstr.objects.all()
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            name = form.cleaned_data['name']
            address_1 = form.cleaned_data['address_1']
            address_2 = form.cleaned_data['address_2']
            city = form.cleaned_data['city']
            pin = form.cleaned_data['pin']
            state_code = form.cleaned_data['state_code']
            gst_no = form.cleaned_data['gst_no']
            pan_aadhar_no = form.cleaned_data['pan_aadhar_no']
            bp_type = form.cleaned_data['bp_type']
            group_code = form.cleaned_data['group_code']
            bsgrp = form.cleaned_data['bsgrp']
            bssubgrp = form.cleaned_data['bssubgrp']
            opbal = form.cleaned_data['opbal']
            clbal = form.cleaned_data['clbal']
            temp_bal = form.cleaned_data['temp_bal']
            user = form.cleaned_data['user']
            upd_time = form.cleaned_data['upd_time']
            share_dep = form.cleaned_data['share_dep']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            pwd = form.cleaned_data['pwd']
            ac_data = AcMstr(code=code, name=name, address_1=address_1, address_2=address_2, city=city, pin=pin, state_code=state_code, gst_no=gst_no, pan_aadhar_no=pan_aadhar_no, bp_type=bp_type, group_code=group_code, bsgrp=bsgrp, bssubgrp=bssubgrp, opbal=opbal, clbal=clbal, temp_bal=temp_bal, user=user, upd_time=upd_time, share_dep=share_dep, email=email, phone=phone, pwd=pwd)
            ac_data.save()
            form = AccountForm()

    else:
        form = AccountForm()

    return render(request, 'accounts.html', {'form': form, 'view': all_items})

def accountsview(request):
    all_items = AcMstr.objects.all()
    #item_filter = ItemFilter(request.GET, queryset=all_items)

    return render(request, 'accountmaster.html', {"view": all_items})



def show(request):
    all_items = ShowMstr.objects.all()
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            show_code = form.cleaned_data['show_code']
            show_name = form.cleaned_data['show_name']
            start_date = form.cleaned_data['start_date']
            show_data = ShowMstr(show_code=show_code, show_name=show_name, start_date=start_date)
            show_data.save()
            all_items = ShowMstr.objects.all()
            form = ShowForm()

    else:
        form = ShowForm()
    return render(request, 'show.html', {'form': form, 'view': all_items})

def showview(request):
    all_items = ShowMstr.objects.all()
    #item_filter = ItemFilter(request.GET, queryset=all_items)

    return render(request, 'showmaster.html', {"view": all_items})

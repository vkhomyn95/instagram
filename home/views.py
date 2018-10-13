# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from home.forms import RegistrationForm


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:home'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)



def upload_photo(request):

    return render(request, 'upload_photo.html', {})


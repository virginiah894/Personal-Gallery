# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render
import datetime as dt


def home(request):
    return render(request,'home.html')

def images_of_day(request):
    date = dt.date.today()
    return render(request, 'all-images/today-images.html', {"date": date,})

def past_days_images(request, past_date):

    try:
        
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(images_of_day)

    return render(request, 'all-images/past-images.html', {"date": date})

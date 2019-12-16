# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render
import datetime as dt
from .models import Image,Location,Category


def home(request):
    return render(request,'home.html')

def images_of_day(request):
    date = dt.date.today()
    images = Image.todays_images()
    return render(request, 'all-images/today-images.html', {"date": date,"images":images})

def past_days_images(request, past_date):

    try:
        
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(images_of_day)
    images= Image.todays_images(date)

    return render(request, 'all-images/past-images.html', {"date": date,"images":images})
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_Name(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-images/onepic.html", {"image":image})

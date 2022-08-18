from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *

def inter(request):

    list_depar_shedul = depart_schedule.objects.order_by('departF_time')[:20]
    list_arrival_schedule = arrival_schedule.objects.order_by('arrivalT_time')[:20]

    list_parking = parking.objects.all()
    list_service = service.objects.all()
    list_store = store.objects.all()


    template = loader.get_template('pool/list.html')
    context = {
        'list_depar_shedul' : list_depar_shedul,
        'list_arrival_schedule' : list_arrival_schedule,
        'list_parking' : list_parking, 
        'list_service' : list_service, 
        'list_store' : list_store,
    }

    return HttpResponse(template.render(context, request))


def rep(request):
    
    list_passanger = passanger.objects.all()


    template = loader.get_template('pool/rep_list.html')
    context = {

        'list_passanger' :list_passanger,

    }

    return HttpResponse(template.render(context, request))

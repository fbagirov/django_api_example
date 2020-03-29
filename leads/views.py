import json
from django.views.generic import View 
#from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import Lead 


def home(request):
    return 'A prorotype for a customer data lead API using Django (non-REST framework)'



class SerializedListViewAll(View):
	def get(self, request, *args, **kwargs):
		json_data = Lead.objects.all().serialize()
		return HttpResponse(json_data, content_type='application/json')


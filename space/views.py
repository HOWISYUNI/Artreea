import json
from .models import *

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize

# Create your views here.
class CompanyListView(View):
    def get(self, request):
        companys = Company.objects.all()
        data = json.loads(serialize('json',companys))
        return JsonResponse({'items':data})
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db import models
from rest_framework.viewsets import ModelViewSet

from .serializers import OrderSerializer


def func(request):
    # newPerson = DatePerson( name = 'Crutoslav', second_name = "Vorobiov", age = 27, numberPhon = '0953650945')
    # newPerson.save()

    # def func(request):
    #     return HttpResponse("<h4> Test </h4>")
    all_users = DatePerson.objects.all()
    print(all_users)
    return render(request, 'HomePageApp/homeHtml.html')


class OrderView(ModelViewSet):
    queryset = DatePerson.objects.all()
    serializer_class = OrderSerializer

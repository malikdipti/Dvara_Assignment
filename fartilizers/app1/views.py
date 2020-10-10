from django.shortcuts import render
from django.views.generic import View,ListView,CreateView
import pandas as pd
from app1.serializers import SubcatagorySerializers,CatagorySerializers
from app1.models import CatagoryModel,SubcatagoryModel,AllDeatilsModel
from rest_framework.views import APIView
from rest_framework.response import Response
import json

class CatagoryClass(APIView):
    def post(self,request):
        data = pd.read_excel('sample_data.xlsx', header=0, index_col='id')
        data1 = data['categories']
        for x, y in data1.items():
            data3 = {"catid":str(x),"Typeofcatagory":y}
            print(data3)
            es = CatagorySerializers(data=data3)
            if es.is_valid():
                es.save()
        message={"mess":"Categories data inserted"}
        return Response(message)

class ViewALL(View):
    def get(self,request):
        return render(request,'viewall.html')


class SubcatagoryClass(APIView):
    def post(self,request):
        a=request.data
        data = pd.read_excel('sample_data1.xlsx', header=0, index_col='catid')
        data1=data['subcategory']
        print(data1)
        for x, y in data1.items():
            result = {"subcatagory":y,"catid":str(x)}
            print(result)
            es = SubcatagorySerializers(data=result)
            if es.is_valid():
                es.save()
        message={"mess":"Subcategories data inserted"}
        return Response(message)

global a
class DashbordClass(View):

    def get(self,request):
        global a
        a=request.GET.get('name')
        # b=request.GET.get('name1')
        # print(a)
        model1=CatagoryModel.objects.all()
        model2=SubcatagoryModel.objects.filter(catid__Typeofcatagory=a)


        return render(request,'dashbord.html',{"model1":model1,"model2":model2,"data":AllDeatilsModel.objects.all()})


class AllClass(View):

    def post(self,request):

        sub=request.POST['name1']
        #print(a)
        ty=request.POST['type']
        #print(cat,ty)
        AllDeatilsModel.objects.create(catagory=a,subcatagory=sub,types=ty)
        return render(request,'dashbord.html',{"data":AllDeatilsModel.objects.all()})
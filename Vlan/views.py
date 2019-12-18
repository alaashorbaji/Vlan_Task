from django.http import HttpResponse
from django.shortcuts import render
import json
from .models import Vlan_T
from .serializer import VlanSerializer
from rest_framework import generics, status
from rest_framework import views
from rest_framework.response import Response
from.command import config
class Show(views.APIView):
    def get(self,request):
         v= Vlan_T.objects.all()
         S=VlanSerializer(v,many=True)
         return Response(S.data)
class show_switch(views.APIView):
    def get(self,request):
        output=config.show()
        return Response(output)

class Create(views.APIView):
    def post(self,request,Vlan_id,Name,Description):
        output=config.comm(Vlan_id,Name,Description)
        m=Vlan_T(Name=Name,Vlan_id=Vlan_id,Description=Description)
        m.save()
        return Response(output)

class Update(views.APIView):
    def put(self,request,Vlan_id,Name):
        output = config.update(Vlan_id, Name)
        m= Vlan_T.objects.get(Vlan_id=Vlan_id)
        m.Name=Name
        m.save()
        return Response(output)

class Delete(views.APIView):
     def delete(self,request,Vlan_id):
         output = config.delete(Vlan_id)
         m= Vlan_T.objects.get(Vlan_id=Vlan_id)
         m.delete()
         return Response(output)


def Home(request):
    return render(request,'Vlan/Vlan.html')
def add(request):
    Vlan_id=request.GET["Vlan_id"]
    Name=request.GET["Name"]
    Description =request.GET["Description"]
    # m = Vlan_T(Name=Name, Vlan_id=Vlan_id, Description=Description)
    # m.save()
    Vlan_table=Vlan_T.objects.all()
    s=VlanSerializer(Vlan_table,many=True)
    s2= json.dumps(s.data)
    print(type(s2))
    return render(request,'Vlan/show.html',{'my_data': s.data})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Person
from .serializers import PersonSerializer

@api_view(['GET'])
def index(request):
    print(request.data)  # to get all data from paylaod
    print(request.data['name']) # to get single key all data from paylaod
    print(request.GET.get("search"))  # if you want to get value from url
    return Response("varDict")

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def people(request):
    if request.method == "GET":
        objs = Person.objects.all()
        serializer = PersonSerializer(objs, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        data = request.data        
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == "PUT":
        data = request.data
        obj = Person.objects.get(id=data["id"])
        serializer = PersonSerializer(objs,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == "PATCH":
        data = request.data
        obj = Person.objects.get(id=data["id"])
        serializer = PersonSerializer(objs, data=data , partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        data = request.data
        obj = Person.objects.get(id=data["id"])
        obj.delete()
        return Response({"message":"person deleted succesfully"})
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from . models import Country 
from .serializers import CountrySerializers

# Create your views here.

@api_view(['GET', 'POST'])
def country(request):
    
    if request.method =='GET': # Request of data
        snippets = Country.objects.all()
        serializer = CountrySerializers(snippets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST': # User posting data
        serializer = CountrySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=staus.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


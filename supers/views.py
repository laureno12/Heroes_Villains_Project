from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super



@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        type=request.queryparams.get("Hero")
        print(type)
        queryset = Super.objects.all()
        if type:
            queryset = supers.filter(type=type)
        
        serializer = SuperSerializer(supers, many=True)
        return Response (serializer.data)
    
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.errors, status =status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT'])
def supers_detail(request, pk):

    super = get_object_or_404(Super, pk=pk)
    if request.method =='GET':
        
        serializer = SuperSerializer(super);
        return Response(serializer.data)
    elif request.method == 'PUT':
        
        serializer = SuperSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    





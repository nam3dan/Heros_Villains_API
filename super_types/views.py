
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SuperType
from .serializers import SuperTypeSerializer

@api_view(['GET','POST'])
def supers_list(request):
    if request.method == "GET":
        queryset = SuperType.objects.all()
        serializer = SuperTypeSerializer(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def super_detail(request, pk):
    supertype = get_object_or_404(SuperType, pk=pk)
    if request.method == 'GET':
        serializer = SuperTypeSerializer(supertype);
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = SuperTypeSerializer(supertype, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        supertype.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
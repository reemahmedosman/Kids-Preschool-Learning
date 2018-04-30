from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .csrf_ignore import CsrfExemptSessionAuthentication,BasicAuthentication
# Create your views here.
class ImageDetailsView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self,request,format=None) :
        data = request.data
        serializer_class = ImageDetailsSerializer(data=data)
        if serializer_class.is_valid():
		#	serializer.create(validated_data=serializer.validated_data)
            serializer_class.save()
            return Response({'valid':True,'errors':'null'}, status=status.HTTP_201_CREATED)
        return Response({'valid':False ,'errors':serializer_class.errors}, status=status.HTTP_400_BAD_REQUEST)

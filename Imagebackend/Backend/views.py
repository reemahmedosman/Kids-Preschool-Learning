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
import cv2,os,shutil
import sys
sys.path.insert(0, 'code/')
import processing

def ReadText():
	folder = "images/cover_photos"
	files = os.listdir(folder)
	image_path = files[0]
	file_path = os.path.join(folder, image_path)
	text = processing.ReadImage(file_path)
	delete_images()	
	return  text

def delete_images(folder = "images/cover_photos"):
	for the_file in os.listdir(folder):
		file_path = os.path.join(folder, the_file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
		except Exception as e:
			print(e)


class ImageDetailsView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self,request,format=None) :
        data = request.data
        serializer_class = ImageDetailsSerializer(data=data)
        # if serializer_class.is_valid():
		# #	serializer.create(validated_data=serializer.validated_data)
        #     serializer_class.save()
        #     return Response({'valid':True,'errors':'null'})
        # return Response({'valid':False ,'errors':serializer_class.errors})
        if serializer_class.is_valid():
            serializer_class.save()
            text = ReadText()
            print (text)
            return Response({'valid':True,'text':text}, status=status.HTTP_201_CREATED)
        print (serializer_class.errors)
        return Response({'valid':False ,'errors':serializer_class.errors}, status=status.HTTP_400_BAD_REQUEST)

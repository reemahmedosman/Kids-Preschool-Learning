
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import *
from drf_extra_fields.fields import Base64ImageField

class ImageDetailsSerializer(serializers.ModelSerializer):
    image = Base64ImageField() 
    class Meta:
        model = ImageDetails
        fields = '__all__'

class WordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Word
		fields = ['text']

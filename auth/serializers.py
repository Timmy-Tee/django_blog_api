from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ['username', 'email', 'password']
          extra_kawrgs = {
               'password': {'write_only': True}
          }
          
     def create(self, validated_data):
          user = User.objects.create_user(**validated_data)
          if user:
               return (user)
          else:
               raise serializers.ValidationError('Error Creating User')
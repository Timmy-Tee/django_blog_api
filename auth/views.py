from rest_framework import mixins, viewsets
from . serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


class UserRegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
     def create(self, request):
          data = request.data
          serializer_class = UserSerializer(data=data)
          
          if serializer_class.is_valid(raise_exception=True):
               serializer_class.save()
               return Response({'message': 'User Successfully Created'}, status=status.HTTP_201_CREATED)
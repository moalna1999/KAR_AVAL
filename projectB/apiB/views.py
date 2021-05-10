from django.shortcuts import render

######################### Import #########################
from rest_framework import viewsets ,generics , status
from .serializers import MemberSerializer,AdminstorSerializer,ForeignKeySerializer,MyTokenObtainPairSerializer,RegisterSerializer
from .models import Adminstors, Members, ForeignKey
from rest_framework.views import APIView
#from . import ViewSet
#from django.http import Http404
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
#from rest_framework.decorators import api_view

from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated ,AllowAny
from rest_framework import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_flex_fields.views import FlexFieldsMixin,FlexFieldsModelViewSet
from rest_flex_fields import is_expanded
from rest_framework.viewsets import ReadOnlyModelViewSet

from django.contrib.auth.models import User
######################### My order #########################
class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

class MembersViewSet(viewsets.ModelViewSet):
  queryset = Members.objects.all().order_by("first_name")
  serializer_class = MemberSerializer
  permission_classes = [IsAuthenticated]

class MyObtainTokenPairView(TokenObtainPairView):
  permission_classes = (AllowAny,)
  serializer_class = MyTokenObtainPairSerializer
#'generics.ListCreateAPIView'

class MembersList(FlexFieldsMixin, ReadOnlyModelViewSet):
  queryset = Members.objects.all()
  serializer_class = MemberSerializer
  filterset_fields = ('id',)
  def get_queryset(self):
    queryset = Members.objects.all()

    if is_expanded(self.request, 'category'):
      queryset = queryset.prefetch_related('category')

    if is_expanded(self.request, 'comments'):
      queryset = queryset.prefetch_related('comments')

    if is_expanded(self.request, 'sites'):
      queryset = queryset.prefetch_related('sites')

    if is_expanded(self.request, 'company'):
      queryset = queryset.prefetch_related('sites__company')

    if is_expanded(self.request, 'productsize'):
      queryset = queryset.prefetch_related('sites__productsize')

    return queryset

class MembersDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Members.objects.all()
  serializer_class = MemberSerializer
    
class AdminstorsViewSet(viewsets.ModelViewSet):
  queryset = Adminstors.objects.all().order_by("name")
  serializer_class = AdminstorSerializer

class ForeignKeyViewSet(viewsets.ModelViewSet):
  queryset = ForeignKey.objects.all().order_by("name")
  serializer_class = ForeignKeySerializer

class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request, *args, **kwargs):
    file_serializer = MemberSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
###########################################
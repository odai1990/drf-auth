from django.db import reset_queries
from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .permission import PermissionsClass
from .models import Moives
from .serializer import MoiveSerializer

class MoviesList(ListAPIView):
    queryset=Moives.objects.all()
    serializer_class=MoiveSerializer

class MoviesDetials(RetrieveAPIView):
    queryset=Moives.objects.all()
    serializer_class=MoiveSerializer


class MoviesCreate(CreateAPIView):
    queryset=Moives.objects.all()
    serializer_class=MoiveSerializer
    permission_classes = (PermissionsClass,)


class MoviesAllOpreations(RetrieveUpdateDestroyAPIView):
    queryset=Moives.objects.all()
    serializer_class=MoiveSerializer
    permission_classes = (PermissionsClass,)

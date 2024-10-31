from django.shortcuts import render
from rest_framework import generics
from .models import Usuarios
from .serializers import UsuariosSerializer
from rest_framework.permissions import IsAuthenticated


class UsuariosListCreate(generics.ListCreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permissions_classes = [IsAuthenticated]

class UsuariosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permissions_classes = [IsAuthenticated]
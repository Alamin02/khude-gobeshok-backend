from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from .models import Contact
from .serializers import ContactSerializer


# Create your views here.
class ContactUsViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

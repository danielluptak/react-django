from django.shortcuts import render
from rest_framework import generics
from .models import Ticket
from django.contrib.auth.models import User
from rest_framework import serializers

# Create your views here.

class TicketSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Ticket
        fields = ['id', 'title', 'body', 'author']
        
class UserSerializer(serializers.ModelSerializer):
    tickets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'tickets']
from django.shortcuts import render
from rest_framework import generics
from .models import Ticket
from django.contrib.auth.models import User
from rest_framework import serializers
from .serializer import TicketSerializer, UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q

# Create your views here.

class TicketList(generics.ListCreateAPIView):
    # queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
    def post(self, serializer):
       
        serializer.save(author=self.request.user)
        
    def get_queryset(self):
        print("USER: ", self.request.user)
        return Ticket.objects.filter(Q(author=self.request.user.id) | Q(it_assigned=self.request.user.id))

    
    # def get(self, request):
    #     tickets = Ticket.objects.filter(author=request.user.id)
    #     serialized_tickets = TicketSerializer(tickets, many=True)
    #     return Response(serialized_tickets.data)
    
    
        
class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRoutes(request):
    routes = [
        '',
        '<int:pk>/',
    ]
    return Response(routes)


from django.urls import path
from . import views

urlpatterns = [
    path('', views.TicketList.as_view()),
    path('<int:pk>/', views.TicketDetail.as_view()),
]

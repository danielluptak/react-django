from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from api.models import Profile
from django.contrib.auth.models import User


# IMPORTANCE_CHOICES = (
#     ('green','I can work, but its bothersome'),
#     ('orange', 'This has created extra steps in order for me to work'),
#     ('red','I cannot work at all'),
# )

# STATUS_CHOICES = (
#     ('new','Ticket reviewed, wait for an IT specialist to respond.'),
#     ('progress', 'Ticket resolution in progress.'),
#     ('closed','Ticket closed.'),
# )

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    # attachment = models.FileField(null=True, blank=True, upload_to="images")
    # status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='new')
    # importance = models.CharField(max_length=50, choices=IMPORTANCE_CHOICES, default='green')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    it_assigned = models.ForeignKey(
        'auth.User',
        # limit_choices_to={'it_for_ticket': True},
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name= 'it_for_ticket'
    )
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['date']

# class TicketIT(models.Model):
#     ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
#     it_assigned = models.ForeignKey(
#         'auth.User',
#         # limit_choices_to={'it_for_ticket': True},
#         null=True,
#         blank=True,
#         on_delete=models.CASCADE,
#         related_name= 'it_for_ticket'
#     )
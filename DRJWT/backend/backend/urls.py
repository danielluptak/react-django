# project_name/urls.py (In my case backend/urls.py)

from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
    path('tickets/', include("Tickets.urls"))
]
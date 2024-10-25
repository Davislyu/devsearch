from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Root URL: routes to projects app URLs
    path('',include('projects.urls'))
   
]

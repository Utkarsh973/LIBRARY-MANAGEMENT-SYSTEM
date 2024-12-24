
from django.contrib import admin
from django.urls import path
from items_app.api import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls )
]

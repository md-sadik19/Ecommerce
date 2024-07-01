
from django.contrib import admin
from django.urls import path,include
from managment.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('managment.urls')),
    path('product/', include('product.urls'))
]

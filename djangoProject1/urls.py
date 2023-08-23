from django.contrib import admin
from django.urls import path, include
from randNum.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('randNum.urls'))
]

handler404 = pageNotFound

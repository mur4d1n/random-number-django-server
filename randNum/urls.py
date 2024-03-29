from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import index, login


urlpatterns = [
    path('', index),
    path('login/', login, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace='social')),
]

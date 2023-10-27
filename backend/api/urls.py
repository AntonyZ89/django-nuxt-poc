from rest_framework import routers
from django.urls import path
from .views import auth

router = routers.DefaultRouter()

auth_urls = [
    path("login", auth.login),
    path("signup", auth.signup)
]

user_urls = []

urlpatterns = router.urls + user_urls + auth_urls

from django.urls import path
from .views import UserDetailView, UserView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
  path("user/",UserView.as_view()),
  path("user/<int:user_id>/",UserDetailView.as_view()),
  path("user/login/", jwt_views.TokenObtainPairView.as_view()),
  ] 
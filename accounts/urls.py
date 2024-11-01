from django.urls import path
from .views import  AccountDetailView, AccountView


urlpatterns = [
  path("account/",AccountView.as_view()),
  path("account/<int:account_id>/",AccountDetailView.as_view()),]
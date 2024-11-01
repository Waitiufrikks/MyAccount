from django.urls import path
from .views import  TransactionDetailView, TransactionView


urlpatterns = [
  path("transaction/",TransactionView.as_view()),
  path("transaction/<int:transaction_id>/",TransactionDetailView.as_view()),
  path("transaction/<int:transaction_id>/deposit/<int:target_account_id>/", TransactionDetailView.as_view()),
  ]
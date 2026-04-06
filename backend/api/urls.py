
from django.contrib import admin
from django.urls import  path

from . import views

urlpatterns = [
path('', views.api_root, name='api-root'),
path('transactions/', views.TransactionListCreateView.as_view(), name='transaction-list-create'),
path('transactions/<uuid:id>/', views.TransactionRetrieveUpdateDestroyView.as_view(), name='transaction-retrieve-update-destroy'),
]




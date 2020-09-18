from django.urls import path
from . import views


urlpatterns = [
    path('company/',views.CompanyListView.as_view(), name = 'company-list')
]
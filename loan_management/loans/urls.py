from django.urls import path
from .views import home, apply_loan, loan_status,user_login, user_logout
from . import views
urlpatterns = [
    path('', home, name='home'),
    path('apply/', apply_loan, name='apply_loan'),
    path('status/', loan_status, name='loan_status'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', views.loan_dashboard, name='loan_dashboard'),
]

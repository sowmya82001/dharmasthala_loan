from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LoanApplication
from .forms import LoanApplicationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.core.mail import send_mail

def home(request):
    return render(request, 'loans/home.html')

@login_required
def apply_loan(request):
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.user = request.user
            loan.save()
            return redirect('loan_status')
    else:
        form = LoanApplicationForm()
    return render(request, 'loans/apply_loan.html', {'form': form})

@login_required
def loan_status(request):
    loans = LoanApplication.objects.filter(user=request.user)  # Show only current user's loans
    return render(request, 'loans/loan_status.html', {'loans': loans})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'loans/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')


def loan_dashboard(request):
    today = now().date()
    loans = LoanApplication.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'loans': loans, 'today': today})

def send_due_payment_reminders():
    today = now().date()
    due_loans = LoanApplication.objects.filter(due_date=today)

    for loan in due_loans:
        send_mail(
            "Loan Payment Due Reminder",
            f"Dear {loan.name},\n\nYour loan payment of Rs. {loan.amount} is due today.\nPlease make the payment to avoid penalties.",
            "admin@loanmanagement.com",  # Replace with your admin email
            [loan.user.email],
            fail_silently=False,
        )
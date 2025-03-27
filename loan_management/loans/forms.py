from django import forms
from .models import LoanApplication

class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = ['name', 'mobile_number', 'address', 'amount', 'purpose', 'interest_rate', 'repayment_term']
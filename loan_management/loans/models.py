from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date
class LoanApplication(models.Model):
    APPLICANT_STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Unknown")
    mobile_number = models.CharField(max_length=15, default="0000000000")
    address = models.TextField(default="Not Provided")
    due_date = models.DateField(null=True, blank=True)  # Loan payment due date
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purpose = models.TextField()
    interest_rate = models.FloatField()
    repayment_term = models.IntegerField(help_text="Repayment term in months")
    status = models.CharField(max_length=10, choices=APPLICANT_STATUS, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = date.today() + timedelta(days=30)  # Default: 30 days from today
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.amount}"
    def __str__(self):
        return f"{self.name} - {self.amount} ({self.status})"
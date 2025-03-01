from django import forms
from .models import Expense  # ✅ Make sure this matches your model name

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'phone', 'email','date']
        widgets = {
            'date':forms.DateInput(attrs={'type': 'date'})
        }

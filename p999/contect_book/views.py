from django.shortcuts import render, redirect
from .models import Contect  # Correct model name
from .forms import ExpensesForm  # Ensure form is using the correct model

def contect_list(request):
    contects = Contect.objects.all()  # Use Contect model
    return render(request, 'contect.html', {'contects': contects})

def add_contect(request):
    if request.method == 'POST':
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contect_list')
    else:
        form = ExpensesForm()
    return render(request, 'add_contect.html', {'form': form})

def update_contect(request, pk):
    contect = Contect.objects.get(pk=pk)  # Use Contect model

    if request.method == 'POST':
        form = ExpensesForm(request.POST, instance=contect)
        if form.is_valid():
            form.save()
            return redirect('contect_list')
    else:
        form = ExpensesForm(instance=contect)
    return render(request, 'update_contect.html', {'form': form})

def delete_contect(request, pk):
    contect = Contect.objects.get(pk=pk)  # Use Contect model
    contect.delete()
    return redirect('contect_list')

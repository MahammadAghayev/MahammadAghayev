from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from .models import ContactInfo
from .forms import AppealingForm
# Create your views here.

def contact(request):
    contact_info = ContactInfo.objects.first()
    form = AppealingForm()
    if request.method == 'POST':
        form = AppealingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Muracietiniz ugurla qeyde alindi, tezlikle sizinle elaqe saxlanilacaq')
            return redirect(reverse_lazy('contact'))

    context = {
        'contact_info' : contact_info,
        'form' : form
    }
    return render(request, 'contact/index.html', context)
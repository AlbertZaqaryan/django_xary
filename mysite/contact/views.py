from django.shortcuts import render, redirect
from .models import ContactUs
from .forms import ContactUsForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            ContactUs.objects.create(**form.cleaned_data)
            return redirect('contact')
    else:
        form = ContactUsForm()
    return render(request, 'contact/contact.html', context={'form':form})


# class ContactFormView(CreateView):
#     template_name = 'contact/contact.html'
#     model = ContactUs
#     fields = ['full_name', 'email', 'company', 'describe']
#     success_url = reverse_lazy('contact')
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Testimonial, Portfolio, Contact
from .forms import ContactForm


def index(request):
    title = ''
    if request.method == 'POST':
        form = ContactForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
            messages.success(request, f'I have got you message. I will get back to you as soon as possible.')
            return redirect('core:index')
    else:
        form = ContactForm()

    testimonials = Testimonial.objects.all().order_by('-id')
    portfolio = Portfolio.objects.all().order_by('-id')
    context = {
        'title': title,
        'testimonials': testimonials,
        'portfolio': portfolio,
        'form': form
    }
    return render(request, 'core/index.html', context)

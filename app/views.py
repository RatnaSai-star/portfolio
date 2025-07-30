from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"New job offering Form form Portfolio {name}"
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            ['ratnasaipeddireddy15@gmail.com'],  # Receiver email
            fail_silently=False
        )
        return redirect('success')  # or render a success page
    return render(request, 'index.html')

def success_view(request):
    return render(request,"success.html")
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render


def home_view(request):
    """Creates view for the hompage"""
    context = {'title': 'Home Page'}
    return render(request, "app1/home.html", context)

def contact(request):
    """Creates contact page form"""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Send email using Django's built-in email sending function
        send_mail(
            'Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        # Render the contact page with a thank you message
        return render(request, 'app1/contact.html', {'thank_you': True})

    return render(request, 'app1/contact.html')

def about(request):
    """Creates about page """
    context = {'title': 'About'}
    return render(request, "app1/about.html", context)





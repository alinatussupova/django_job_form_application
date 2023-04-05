from django.shortcuts import render
from .forms import ApplicationForm, ContactForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage
from decouple import config


EMAIL_HOST_USER = config("EMAIL_HOST_USER")


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            status = form.cleaned_data["status"]

            # Store data in the database    
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, status=status)
            
            message_body = f"A new job application was submitted! \n{first_name} {last_name} \nThank you!"
            email_message = EmailMessage("Form submission confirmation", message_body, to=[email])
            email_message.send()
            
            # Show a message after submitting a form            
            messages.success(request, "Form submitted successfully!")

    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            message_body = f"{subject}. From: {email} \n{message} \n{first_name} {last_name}"
            email_message = EmailMessage("New message", message_body, to=[EMAIL_HOST_USER])
            email_message.send()

            messages.success(request, "Your message was successfully submitted! Thank you!")
    return render(request, "contact.html")

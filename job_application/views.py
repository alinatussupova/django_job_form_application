from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages


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
            
            # Show a message after submitting a form            
            messages.success(request, "Form submitted successfully!")


    return render(request, "index.html")

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Meetup
from .forms import RegistrationForm

# Create your views here.

def home(request):
    meetups = Meetup.objects.all()

    return render(request, "meetup/home.html", {
        'meetups': meetups
        }
    )


def meetup_details(request, meetup_slug):
    try:
        
        selected_meetup = Meetup.objects.get(slug=meetup_slug)

        if request.method == "GET":

            return render(request, "meetup/meetup-details.html", {
                'meetup_found': True,
                'meetup': selected_meetup,
                'registration': RegistrationForm()
                }
            )
        else:
            '''
            We get access to the data by accessing request to read some data from the request.
            .POST give us access to the data itself. 
            POST will hold a dictionary with the keys being the names assigned to the input and 
            the values are the entered values.
            Here we are passing the data entered by the user into the form, this allows us use  
            form.is_valid().
            '''
            registration = RegistrationForm(request.POST)

            if registration.is_valid():
                # This will only enable us to use an email address once across all meetups
                # This will return an instance of the save model
                participant = registration.save()
                # This adds the participant and email to the specific meetup
                selected_meetup.participants.add(participant)
                return redirect("registration-confirmation")

            return render(request, "meetup/meetup-details.html", {
                'meetup_found': True,
                'meetup': selected_meetup,
                'registration': RegistrationForm()
                }
            )

    except Exception as exc:
        return render(request, "meetup/meetup-details.html", {
            'meetup_found': False
            }
        )


def confirm_registration(request):
    meetups = Meetup.objects.all()
    
    return render(request, "meetup/registration-success.html", {
        'meetups': meetups
        }
    )
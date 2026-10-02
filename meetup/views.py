from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Meetup, Participant
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
                # registration.save() will only enable us to use an email address once across all meetups
                # participant = registration.save() will return an instance of the save model
                # participant = registration.save()

                # get the participant email
                user_email = registration.cleaned_data['email']

                # get_or_create() allows us to create a new instance of an object if it doesn't exist, or use the existing object if it does exist
                # get_or_create() returns a tuple where we get the created or identified object and a flag that tells us if a new entry was created
                # with this participant, _ = we are unpacking the tuple
                # The underscore _ tells us to ignore the second value (the flag)
                participant, _ = Participant.objects.get_or_create(email=user_email)
                # This adds the participant and email to the specific meetup
                selected_meetup.participants.add(participant)
                # meetup_slug= as defined in the  url
                return redirect("registration-confirmation", meetup_slug=meetup_slug)

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


def confirm_registration(request, meetup_slug):
    meetups = Meetup.objects.all()
    
    return render(request, "meetup/registration-success.html", {
        'meetups': meetups
        }
    )
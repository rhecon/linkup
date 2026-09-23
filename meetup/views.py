from django.shortcuts import render
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
from django import forms
from .models import Participant


class RegistrationForm(forms.ModelForm):
    # This django the Model class the form should be related
    class Meta:
        model = Participant
        # Specifies the fields in the model that should make up the form
        # If you want to include all the fields, you can do this fields = "__all__"
        # If you want to render specific fields, yo can do this fields = ['user_name', 'user_email', 'comment_text']
        # If you want to render all fields except one or two you can do this exclude = ['owner_comment', 'checked'] 
        fields = "__all__"

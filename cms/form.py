from django import forms
from django.core.validators import RegexValidator

PHONE_NUMBER_REGEX = r"^(601)[0-46-9][0-9]{7,8}$"
PHONE_NUMBER_VALIDATOR = RegexValidator(
    regex=PHONE_NUMBER_REGEX,
    message="Phone number must be entered in the format '60123456789'. Up to 12 digits allowed.",
)


class ContactForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    email = forms.EmailField(label="Your email")  # Fixed label here
    mobile_number = forms.CharField(label="Mobile number", max_length=64)
    type_of_enquiry = forms.CharField(max_length=100)
    message = forms.CharField(max_length=1048)

    widgets = {
        "your_name": forms.TextInput(attrs={"placeholder": "Your Name"}),
        "email": forms.EmailInput(
            attrs={"class": "input-register", "placeholder": "youremail@example.com"}
        ),
        "mobile_number": forms.TextInput(
            attrs={"class": "input-register", "placeholder": "Your Mobile Number"}
        ),
        "type_of_enquiry": forms.Select(attrs={"class": "input-select"}),
        "subject": forms.TextInput(
            attrs={"class": "input-register", "placeholder": "Enter a Subject"}
        ),
        "message": forms.Textarea(
            attrs={
                "class": "input-register input-details-height",
                "placeholder": "Enter Message Here...",
            }
        ),
    }

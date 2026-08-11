from django import forms
from .models import ContactMessage, Application


class ContactMessageForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email'
            }),

            'message': forms.Textarea(attrs={
                'placeholder': 'Write your message here...'
            }),
        }


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application

        fields = [
            'student_name',
            'date_of_birth',
            'class_applying_for',
            'parent_name',
            'phone',
            'email',
            'address',
            'previous_school',
            'message',
        ]

        widgets = {

            'student_name': forms.TextInput(attrs={
                'placeholder': 'Enter student name'
            }),

            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'class_applying_for': forms.TextInput(attrs={
                'placeholder': 'e.g. Grade 5'
            }),

            'parent_name': forms.TextInput(attrs={
                'placeholder': 'Enter parent/guardian name'
            }),

            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter phone number'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email address'
            }),

            'address': forms.Textarea(attrs={
                'placeholder': 'Enter your address',
                'rows': 3
            }),

            'previous_school': forms.TextInput(attrs={
                'placeholder': 'Enter previous school (if applicable)'
            }),

            'message': forms.Textarea(attrs={
                'placeholder': 'Any additional information...',
                'rows': 4
            }),
        }


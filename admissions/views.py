from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactMessageForm, ApplicationForm
from .models import Scholarship, Announcement


def index(request):
    return HttpResponse('Welcome to Einstein Public School')


def home(request):
    latest_announcements = Announcement.objects.filter(
        published=True
    ).order_by('-date')[:3]

    return render(
        request,
        'home.html',
        {
            'latest_announcements': latest_announcements
        }
    )


def procedure(request):
    return render(request, 'procedure.html')


def about(request):
    return render(request, 'about.html')

def founder_message(request):
    return render(request, 'founder-message.html')


def contact(request):

    if request.method == 'POST':

        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/admissions/contact/?success=1')

    else:
        form = ContactMessageForm()

    return render(request, 'contact.html', {'form': form})


def apply(request):

    if request.method == 'POST':

        form = ApplicationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/admissions/apply/?success=1')

    else:
        form = ApplicationForm()

    return render(request, 'apply.html', {'form': form})


def scholarships(request):
    scholarship_list = Scholarship.objects.all()

    return render(
        request,
        'scholarships.html',
        {'scholarships': scholarship_list}
    )


def announcements(request):
    announcement_list = Announcement.objects.filter(
        published=True
    ).order_by('-date')

    return render(
        request,
        'announcements.html',
        {'announcements': announcement_list}
    )


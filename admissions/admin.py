from django.contrib import admin
from .models import (
    Admission,
    Scholarship,
    ContactMessage,
    Application,
    Announcement,
)


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'student_name',
        'class_applying_for',
        'parent_name',
        'phone',
        'email',
        'created_at',
    )

    search_fields = (
        'student_name',
        'parent_name',
        'email',
        'phone',
    )

    ordering = ('-created_at',)


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'published',
    )

    list_filter = (
        'published',
        'date',
    )

    search_fields = (
        'title',
        'content',
    )

    ordering = ('-date',)



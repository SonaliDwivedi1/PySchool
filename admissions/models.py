from django.db import models


class Admission(models.Model):
    name = models.CharField(max_length = 255)
    about = models.TextField()
    values = models.TextField()
    image_url = models.CharField(max_length = 2083)

    def __str__(self):
        return self.name


class Scholarship(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    eligibility = models.TextField()
    amount = models.TextField()

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Application(models.Model):

    student_name = models.CharField(max_length=255)

    date_of_birth = models.DateField()

    class_applying_for = models.CharField(max_length=100)

    parent_name = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)

    email = models.EmailField()

    address = models.TextField()

    previous_school = models.CharField(
        max_length=255,
        blank=True
    )

    message = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.student_name


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title



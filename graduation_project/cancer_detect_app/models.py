from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    national_id = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    institution = models.CharField(max_length=100)

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    bmi = models.IntegerField()
    FOBT_CHOICES = [
        ('positive', 'Positive'),
        ('negative', 'Negative'),
    ]
    fobt = models.CharField(max_length=10, choices=FOBT_CHOICES)
    DIABETES_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    diabetes = models.CharField(max_length=10, choices=DIABETES_CHOICES)
    VEGETARIAN_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    vegetarian = models.CharField(max_length=10, choices=VEGETARIAN_CHOICES)
    SMOKING_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    smoking = models.CharField(max_length=10, choices=SMOKING_CHOICES)
    library_size_wirbel = models.IntegerField()
    library_size_raw = models.IntegerField()
    library_size_filtered = models.IntegerField()
    SAMPLE_TAKEN_CHOICES = [
        ('left colon', 'Left Colon'),
        ('Right colon', 'Right Colon'),
        ('Rectum', 'Rectum'),
        ('left and right colon and rectum', 'Left and Right Colon and Rectum'),
        ('left and right colon', 'Left and Right Colon'),
    ]
    sample_taken = models.CharField(max_length=50, choices=SAMPLE_TAKEN_CHOICES)
    test_result = models.TextField()

    def __str__(self):
        return self.name

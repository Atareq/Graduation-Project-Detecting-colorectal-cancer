# Generated by Django 4.2.3 on 2023-08-27 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('national_id', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('institution', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('bmi', models.IntegerField()),
                ('fobt', models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], max_length=10)),
                ('diabetes', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('vegetarian', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('smoking', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('library_size_wirbel', models.IntegerField()),
                ('library_size_raw', models.IntegerField()),
                ('library_size_filtered', models.IntegerField()),
                ('sample_taken', models.CharField(choices=[('left colon', 'Left Colon'), ('Right colon', 'Right Colon'), ('Rectum', 'Rectum'), ('left and right colon and rectum', 'Left and Right Colon and Rectum'), ('left and right colon', 'Left and Right Colon')], max_length=50)),
                ('test_result', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

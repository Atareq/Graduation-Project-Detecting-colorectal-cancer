from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile, TestResult
from django.contrib.auth import authenticate, login
from .forms import TestForm
from django.contrib.auth.decorators import login_required
from . import ml_data
from django.contrib import messages
import logging
import numpy as np


def home(request):
    context = {}
    return render(request, "index.html", context)


def about(request):
    context = {}
    return render(request, "About_us.html", context)


def help(request):
    context = {}
    return render(request, "Help.html", context)


def contact(request):
    context = {}
    return render(request, "Contact.html", context)


def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        national_id = request.POST["id"]
        city = request.POST["city"]
        email = request.POST["email"]
        gender = request.POST["gender"]
        # institution = request.POST['institution']
        print(request.POST)
        password = request.POST["password"]

        user = User.objects.create_user(
            username=email,
            password=password,
            email=email,
            first_name=name,
            last_name=phone,
        )
        profile = UserProfile.objects.create(
            user=user,
            city=city,
            national_id=national_id,
            gender=gender,
            # institution=institution
        )

        user.save()
        profile.save()

        return redirect("login")
    return render(request, "sign_up.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["pass"]

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # Redirect to colon model page instead of home
            return redirect("profile")
        else:
            return render(request, "login.html", {"error": "Invalid email or password"})

    return render(request, "login.html")


@login_required
def profile(request):
    print(request.user)
    user = User.objects.get(email=request.user)
    profile = UserProfile.objects.get(user=user)
    test_results = TestResult.objects.filter(user=request.user)

    lst = []
    for obj in test_results:
        lst.append([obj.id, obj.name, obj.age, obj.test_result])
        # lst.append([obj.id,obj.name,obj.age,obj.test_result])
    print(lst)
    context = {
        "name": user.first_name,
        "ID": profile.national_id,
        "patient_list": lst,
    }

    return render(request, "profile.html", context=context)


@login_required
def edit_test_result(request, test_result_id):
    test_result = get_object_or_404(TestResult, id=test_result_id, user=request.user)

    if request.method == "POST":
        form = TestForm(request.POST, instance=test_result)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = TestForm(instance=test_result)

    return render(request, "edit_test_result.html", {"form": form})


@login_required
def delete_test_result(request, test_result_id):
    test_result = get_object_or_404(TestResult, id=test_result_id, user=request.user)

    if request.method == "POST":
        test_result.delete()
        return redirect("profile")

    return render(request, "delete_test_result.html", {"test_result": test_result})


@login_required
def profile_info(request):
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            test_result = form.save(commit=False)
            test_result.user = request.user
            test_result.save()
            data = form.cleaned_data

            #####################################################################################################################
            # res = 3
            res = ml_data.ml_result(data)
            # Define the array
            array = np.array(res)

            # Check the first item and assign positive/negative based on the condition
            if array[0, 0] > 0.95:
                output = "positive"
            else:
                output = "negative"
            """
            # Check the second item and update the output based on the condition
            if array[0, 1] > 0.8:
                output = "stage 4"

            # Print the output
            print(output)

            """
            user = TestResult.objects.filter(name=data["name"]).first()
            user.test_result = output
            user.save()

            # Add a success message
            logger = logging.getLogger()
            logger.info(output)
            return redirect("profile")

    else:
        form = TestForm()
    return render(request, "profile-info.html", {"form": form})


def search_results(request):
    pass

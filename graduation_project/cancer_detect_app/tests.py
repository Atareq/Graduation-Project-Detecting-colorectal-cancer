from unittest import mock

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import TestResult

FORM_DATA = {
    "name": "Ahmed",
    "age": 61,
    "gender": "male",
    "bmi": 27,
    "fobt": "positive",
    "diabetes": "No",
    "vegetarian": "No",
    "smoking": "Yes",
    "library_size_wirbel": 124,
    "library_size_raw": 1234,
    "library_size_filtered": 124,
    "sample_taken": "Rectum",
}


class ProfileInfoTests(TestCase):
    def submit(self, username, prediction):
        user = User.objects.create_user(username=username, password="pass")
        self.client.force_login(user)
        with mock.patch(
            "cancer_detect_app.ml_data.ml_result", return_value=[prediction]
        ):
            self.client.post(reverse("profile_info"), FORM_DATA)
        return TestResult.objects.get(user=user)

    def test_prediction_is_saved_on_the_submitted_record(self):
        first = self.submit("first", [0.99, 0.1])
        second = self.submit("second", [0.10, 0.1])

        first.refresh_from_db()
        self.assertEqual(first.test_result, "positive")
        self.assertEqual(second.test_result, "negative")

# Colorectal Cancer Risk Prediction

Graduation project: a Django web app where a clinician records a patient's
clinical data and a trained scikit-learn model returns a positive or
negative colorectal cancer prediction.

Python 3.11 · Django 4.2 · scikit-learn 1.2.2 · pandas · Django templates ·
Jazzmin admin

## What it does

- Users register, log in, and keep a profile (city, national ID,
  institution).
- A test form records a patient's age, gender, BMI, faecal occult blood test
  (FOBT) result, diabetes, diet, smoking, three library-size features, and
  where the sample was taken.
- The inputs are encoded into the model's feature layout and scored by a
  random-forest multi-output model stored in
  `cancer_detect_app/model_file.pkl`. A first output above 0.95 is reported
  as positive.
- Each user sees, edits and deletes only their own test results.

The prediction code is in
[`cancer_detect_app/ml_data.py`](graduation_project/cancer_detect_app/ml_data.py)
and the form handling in
[`cancer_detect_app/views.py`](graduation_project/cancer_detect_app/views.py).

## Running locally

```bash
cd graduation_project
python3.11 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

scikit-learn is pinned to 1.2.2 because the model was saved with that
version. Run the tests with `python manage.py test`.

## Limitations

- An academic prototype, not a validated medical tool.
- Development settings only: `DEBUG = True` and a hard-coded secret key.
- Each prediction writes its encoded input to a shared file
  (`cancer_detect_app/test.txt`) before scoring, so concurrent requests can
  overwrite each other's input.
- The training data and training code are not in this repository.

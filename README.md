# FakeFacesSurvey
 
This code is for a survey webapp that was used for the research behind the study 'Testing Human Ability to Detect "Deepfake" Images of Human Faces'.


To run the webapp, complete the following steps:

1) Download the code
2) Make sure Django is installed (`pip install django`)
3) Navigate to the location of the `manage.py` file (`cd ./survey1/`)
4) Run `python manage.py makemigrations`, `python manage.py migrate`, and `python manage.py populate_imgs`
5) Now the webapp should be ready to run: serve it to `127.0.0.1:8000` by running `python manage.py runserver`
6) Navigate to `127.0.0.1` (which will redirect to `127.0.0.1:8000/surveyapp/intro.html`) in any web browser to test the survey

import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class SubmitResponse(forms.Form):
    image = forms.CharField()
    choice = forms.ChoiceField(choices=[('real','Real'),('ai','AI-generated')],widget=forms.RadioSelect)
    confidence = forms.ChoiceField(choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9')],widget=forms.RadioSelect)
    reasoning = forms.CharField()
    heatmapFill = forms.CharField()

    def clean_response_date(self):
        data = self.cleaned_data['reasoning','choice','confidence','heatmapFill','image']
        # Remember to always return the cleaned data.
        return data


class Greetings(forms.Form):
    one = forms.BooleanField(label="Welcome. We hope you are having a good day so far.", required=False)
    two = forms.BooleanField(label="Welcome, and thank you for participating in our study.", required=False)
    three = forms.BooleanField(label="Welcome, thank you for participating in our study. We hope you enjoy taking part.", required=False)
    four = forms.BooleanField(label="Welcome. We hope that you are sitting comfortably.", required=False)
    five = forms.BooleanField(label="Welcome! We hope the sun is shining where you are.", required=False)


class Thanks(forms.Form):
    one = forms.BooleanField(label="Thank you for completing our survey.", required=False)
    two = forms.BooleanField(label="Many thanks from the research team behind this survey.", required=False)
    three = forms.BooleanField(label="Thank you for participating in this survey.", required=False)
    four = forms.BooleanField(label="Thank you - your participation is greatly appreciated.", required=False)
    five = forms.BooleanField(label="Many thanks for completing the survey.", required=False)


class InformedConsent(forms.Form):
    voluntary = forms.BooleanField(label="I understand that my participation is voluntary and that I can stop the survey at any time without giving a reason.", required=True)
    unremoveable = forms.BooleanField(label="I understand that once I have submitted my answers, my responses can’t be removed.")
    anonymous = forms.BooleanField(label="I understand that I remain fully anonymous, and that I won’t be identifiable in any publications or reports on the results of this study.")
    publishable = forms.BooleanField(label="I understand that the results of this survey will be reported in academic publications or conference presentations.")
    benefits = forms.BooleanField(label="I understand the direct/indirect benefits of participating.")
    nomoney = forms.BooleanField(label="I understand that, beyond the initial and potential bonus fee via the Prolific platform, I will not benefit financially from this study or from any possible outcome it may result in in the future.")
    complaint = forms.BooleanField(label="I am aware of who I should contact if I wish to lodge a complaint (email address: s.bray@cs.ucl.ac.uk).")

    def clean_retrospective_date(self):
        data = {self.cleaned_data['voluntary'], self.cleaned_data['unremoveable'], self.cleaned_data['anonymous'],
                self.cleaned_data['publishable'], self.cleaned_data['benefits'], self.cleaned_data['nomoney'],
                self.cleaned_data['complaint'],}

        # Remember to always return the cleaned data.
        return data


class ProlificID(forms.Form):
    enterID = forms.CharField(label="Please input your Prolific ID before continuing:")

    def clean_retrospective_date(self):
        data = {self.cleaned_data['enterID']}
        return data

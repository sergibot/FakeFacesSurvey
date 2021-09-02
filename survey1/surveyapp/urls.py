from django.urls import path
from surveyapp.views import mainQuPage, introPage, familiarizationPage, helpPage, taskInstructions, exampleTask, \
    consent, greetingQu, dataProtection, bonusPaymentInfo

urlpatterns = [
    path('intro', introPage, name='intro'),
    path('taskInstructions', taskInstructions, name='taskInstructions'),
    path('exampleTask', exampleTask, name='exampleTask'),
    path('introFamiliarization', familiarizationPage, name='introFamiliarization'),
    path('introHelp', helpPage, name='introHelp'),
    path('greetingQu', greetingQu, name='greetingQu'),
    path('main', mainQuPage, name='main1'),
    path('consent', consent, name='consent'),
    path('dataProtection', dataProtection, name='dataProtection'),
    path('bonusPaymentInfo', bonusPaymentInfo, name='bonusPaymentInfo'),
]

handler500 = 'surveyapp.views.handler500'
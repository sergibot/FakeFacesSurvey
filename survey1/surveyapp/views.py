import datetime
import random

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from surveyapp.forms import SubmitResponse, InformedConsent, Greetings, ProlificID, Thanks
from surveyapp.models import Image, Participant, Response, AdviceStartTime, AdviceEndTime
from django.template import RequestContext


def handler500(request, *args, **argv):
    response = render(None,'500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response


def index(request):
    return HttpResponse("Hello, you've somehow reached the index page. Please go to .../intro instead of .../index")


def introPage(request):
    print('start page')

    cons_so_far = AdviceStartTime.objects.all()
    ppants_consented = []
    for c in cons_so_far:
        ppants_consented += [c.ppant_id]

    request.session['numsYet'] = []
    ppants = Participant.objects.all()

    assign_category = random.choice(['A','B','C','D'])
    print("assigning this ppant to",assign_category)

    request.session['category'] = assign_category

    ppant_rand = random.randint(0, 999999)+1
    while ppant_rand in [p.ppant_id for p in ppants]:
        ppant_rand = random.randint(0, 999999) + 1

    request.session['ppant_id'] = ppant_rand
    print("ppant is:",ppant_rand)

    form = ProlificID()
    context = {
        'form': form,
    }

    if request.method == 'POST':
        print("posting")
        ppant_id = request.session.get('ppant_id', 'default')
        print("ppant is:",ppant_id)
        time_now = datetime.datetime.now()
        category = request.session.get('category', 'default')

        form = ProlificID(request.POST)
        if form.is_valid():
            print("form valid")
            prolificID = form.cleaned_data['enterID']
            ppant_instance = Participant(
                ppant_id = ppant_id,
                prolificID = prolificID,
                time_started = time_now,
                category = category)
            ppant_instance.save()
            return redirect(taskInstructions)
        else:
            print("FORM INVALID")

    return render(request, 'entrancePage.html', context=context)


def consent(request):
    form = InformedConsent()

    context = {
        'form': form,
        'ppant_id': request.session.get('ppant_id', 'default'),
    }

    if request.method == 'POST':
        return redirect(bonusPaymentInfo)

    return render(request, 'consent.html', context=context)


def bonusPaymentInfo(request):
    category = request.session.get('category', 'default')
    if request.method == 'POST':
        time_now = datetime.datetime.now()
        this_ppant_id = request.session.get('ppant_id', 'default')
        ppant_query = Participant.objects.filter(ppant_id=this_ppant_id)
        for i in ppant_query:
            ppant_instance = i
        advice_type_dict = {'A':'control','B':'familiarization','C':'help','D':'help also at qu level'}
        advice_time_instance = AdviceStartTime(
            ppant_id=ppant_instance,
            advice_type=advice_type_dict[category],
            time_at_submission=time_now
        )
        advice_time_instance.save()
        print(category)
        if category == 'A':
            return redirect(greetingQu)
        if category == 'B':
            return redirect(familiarizationPage)
        if category == 'C' or category == 'D':
            return redirect(helpPage)

    return render(request, 'bonusPaymentInfo.html')


def taskInstructions(request):
    return render(request, 'taskInstructions.html')


def exampleTask(request):
    context = {
        'category': request.session.get('category', 'default'),
    }
    return render(request, 'exampleTask.html', context=context)


def dataProtection(request):
    return render(request, 'dataProtection.html')


def familiarizationPage(request):
    randomTwenty = ['1', '2', '3', '4', '5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    random.shuffle(randomTwenty)

    if request.method == 'POST':
        # submit to database timelog of: advicetype, participantid, time
        time_now = datetime.datetime.now()
        this_ppant_id = request.session.get('ppant_id', 'default')
        ppant_query = Participant.objects.filter(ppant_id=this_ppant_id)
        for i in ppant_query:
            ppant_instance = i
        advice_time_instance = AdviceEndTime(
            ppant_id=ppant_instance,
            advice_type='control',
            time_at_submission=time_now
        )
        advice_time_instance.save()
        return redirect(mainQuPage)

    context = {
        'randomTwenty': randomTwenty,
    }
    return render(request, 'introfamiliarization.html', context=context)


def helpPage(request):
    maj = ['a', 'b', 'c']
    random.shuffle(maj)
    minA = ['1', '2', '3']
    random.shuffle(minA)
    minB = ['1', '2', '3', '4']
    random.shuffle(minB)
    minC = ['1', '2', '3']
    random.shuffle(minC)

    if request.method == 'POST':
        # submit to database timelog of: advicetype, participantid, time
        time_now = datetime.datetime.now()
        print("Help",time_now)
        this_ppant_id = request.session.get('ppant_id', 'default')
        ppant_query = Participant.objects.filter(ppant_id=this_ppant_id)
        for i in ppant_query:
            ppant_instance = i
        advice_time_instance = AdviceEndTime(
            ppant_id=ppant_instance,
            advice_type='control',
            time_at_submission=time_now
        )
        advice_time_instance.save()
        return redirect(mainQuPage)

    context = {
        'maj': maj,
        'minA': minA,
        'minB': minB,
        'minC': minC,
    }
    return render(request, 'introhelp.html', context=context)


def greetingQu(request):
    form = Greetings()
    form_thanks = Thanks()
    context = {
        'form': form,
        'form_thanks': form_thanks,
    }
    if request.method == 'POST':
        # submit to database timelog of: advicetype, participantid, time
        time_now = datetime.datetime.now()
        this_ppant_id = request.session.get('ppant_id', 'default')
        ppant_query = Participant.objects.filter(ppant_id=this_ppant_id)
        for i in ppant_query:
            ppant_instance = i
        advice_time_instance = AdviceEndTime(
            ppant_id = ppant_instance,
            advice_type = 'control',
            time_at_submission = time_now
        )
        advice_time_instance.save()
        return redirect(mainQuPage)
    return render(request, 'greetingQu.html', context=context)


def mainQuPage(request):
    time_now = datetime.datetime.now()
    print("MAINQUPAGE")
    how_many_qus = 20

    this_ppant_id = request.session.get('ppant_id', 'default')
    ppant_query = Participant.objects.filter(ppant_id=this_ppant_id)
    for i in ppant_query:
        ppant_instance = i

    img_nums_so_far_this_ppant = []

    try:
        responses_by_this_ppant = Response.objects.filter(ppant_id=ppant_instance)
        for j in responses_by_this_ppant:
            img_num = str(j.image_id)[5:]
            img_nums_so_far_this_ppant += [img_num]
    except:
        print("something failed in response table...")

    print("This ppant has seen these imgs:",img_nums_so_far_this_ppant)
    print("Ppant", this_ppant_id, "has so far completed", len(img_nums_so_far_this_ppant), "questions.")

    # AFTER ALL QUESTIONS COMPLETE, END SURVEY.
    if len(img_nums_so_far_this_ppant) > (how_many_qus-1):
    # if len(img_nums_so_far_this_ppant) > 1:
        return render(request, 'endsurvey.html')
    imgs = Image.objects.all()

    print("any POST:")
    print(request.POST)
    if request.method == 'POST':
        print("POSTING")
        form = SubmitResponse(request.POST)

        if form.is_valid():
            print("FORM VALID")
            this_ppant_id = request.session.get('ppant_id', 'default')
            ppant_query = Participant.objects.filter(ppant_id= this_ppant_id)
            for i in ppant_query:
                ppant_instance = i
            img_this = form.cleaned_data['image']
            img_full_id = 'image'+str(img_this)
            print(img_full_id)
            image_instance = img_full_id

            resp_rand = random.randint(0, 99999) + 1
            try:
                resps = Response.objects.all()
                while resp_rand in [r.response_id for r in resps]:
                    resp_rand = random.randint(0, 99999) + 1
            except:
                print("something went wrong with response table")

            response_instance = Response(
                time_at_submission=time_now,
                response_id = resp_rand,
                ppant_id = ppant_instance,
                image_id = image_instance,
                choice = form.cleaned_data['choice'],
                confidence = form.cleaned_data['confidence'],
                reasoning = form.cleaned_data['reasoning'],
                heatmapFill = form.cleaned_data['heatmapFill'],
            )
            response_instance.save()

            return HttpResponseRedirect(reverse('main1'))
        else:
            print("FORM INVALID")
    else:
        print("GET request.")
        form = SubmitResponse()
    maj = ['HELPa', 'HELPb', 'HELPc']
    random.shuffle(maj)
    minA = ['1', '2', '3']
    random.shuffle(minA)
    minB = ['1', '2', '3', '4']
    random.shuffle(minB)
    minC = ['1', '2', '3']
    random.shuffle(minC)

    soFar = img_nums_so_far_this_ppant
    print("sofar:",soFar)
    rand = random.randint(0, 99) + 1
    print("rand=",rand)
    # if soFar != 'default':
    request.session['numsYet'] = img_nums_so_far_this_ppant
    if soFar != []:
        while str(rand) in soFar:
            print("skipping", rand)
            rand = random.randint(0, 99) + 1

        request.session['numsYet'] += [rand]
    else:
        request.session['numsYet'] = [rand]

    print("yes rand=",rand)


    context = {
        'maj': maj,
        'minA': minA,
        'minB': minB,
        'minC': minC,
        'imgs': imgs,
        'category': request.session.get('category', 'default'),
        'numsYet': request.session.get('numsYet', 'default'),
        'num': rand,
        'form': form,
        'ppant_id': request.session.get('ppant_id', 'default'),
    }

    return render(request, 'page1.html', context=context)



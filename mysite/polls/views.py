from django.shortcuts import render
from django.http import Http404
# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404
# from django.template import loader


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] # display latest 5 poll questions
    # template = loader.get_template('polls/index.html') # loads index.html

    # The context is a dictionary mapping template variable names to Python objects.
    context = {'latest_question_list': latest_question_list,}

    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context) # Loader & HttpResponse not required when using render(), render does it for you

def detail(request, question_id):
    # The view raises the Http404 exception if a question with the requested ID doesn’t exist.

    #For this import Http404
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})

    # Shortcut --> import get_object_or_404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
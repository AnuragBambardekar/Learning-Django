from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# We’re using two generic views here: ListView and DetailView. 
# Respectively, those two views abstract the concepts of “display a list of objects” and “display a detail page for a particular type 
# of object.”
# Each generic view needs to know what model it will be acting upon. This is provided using the model attribute.
# The DetailView generic view expects the primary key value captured from the URL to be called "pk", so we’ve changed 
# question_id to pk for the generic views.

class IndexView(generic.ListView):
    template_name = 'polls/index.html' # use our existing "polls/index.html" template.
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5] #bug

        # eturns a queryset containing Questions whose pub_date is less than or equal to - that is, earlier than or equal to - timezone.now.
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5] 


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html' # uses the template "polls/question_detail.html"
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now()) # lte = less than or equal to


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now()) # lte = less than or equal to


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# from django.shortcuts import render
# from django.http import Http404
# # Create your views here.
# from django.http import HttpResponse, HttpResponseRedirect
# from .models import Question, Choice
# from django.shortcuts import get_object_or_404
# from django.urls import reverse
# from django.template import loader


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5] # display latest 5 poll questions
#     # template = loader.get_template('polls/index.html') # loads index.html

#     # The context is a dictionary mapping template variable names to Python objects.
#     context = {'latest_question_list': latest_question_list,}

#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context) # Loader & HttpResponse not required when using render(), render does it for you

# def detail(request, question_id):
#     # The view raises the Http404 exception if a question with the requested ID doesn’t exist.

#     #For this import Http404
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question': question})

#     # Shortcut --> import get_object_or_404
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#     # return HttpResponse("You're looking at question %s." % question_id)

# def results(request, question_id):
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# def vote(request, question_id):
#     # return HttpResponse("You're voting on question %s." % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice']) # request.POST['choice'] returns the ID of the selected choice, as a string.
#         # Checks for KeyError and redisplays the question form with an error message if choice isn’t given.
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         # After incrementing the choice count, the code returns an HttpResponseRedirect rather than a normal HttpResponse.
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.

#         # reverse function helps avoid having to hardcode a URL in the view function. 
#         # It is given the name of the view that we want to pass control to and the variable 
#         # portion of the URL pattern that points to that view.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
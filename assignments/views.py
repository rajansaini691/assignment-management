from django.shortcuts import render

from .forms import AssignmentForm, QuestionForm, QuestionComponentForm, AnswerForm

# TODO  Follow google docs url schema (assignment creation redirects to edit view, where
#       user adds stuff. Associated with assignment pk)
# Create your views here.
def create_assignment(request):
    context = {
        'assignment_form': AssignmentForm(),
        'question_form': QuestionForm(),
        'question_component_form': QuestionComponentForm(),
        'answer_form': AnswerForm()
    }

    return render(request, 'assignments/create_assignment.html', context)

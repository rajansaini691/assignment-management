from django.forms import ModelForm

from .models import Assignment, Question, QuestionComponent, Answer

class AssignmentForm(ModelForm):
    class Meta:
        fields = ["title"]
        model = Assignment

class QuestionForm(ModelForm):
    class Meta:
        fields = []
        model = Question

class QuestionComponentForm(ModelForm):
    class Meta:
        fields = ["component_type", "text"]
        model = QuestionComponent

class AnswerForm(ModelForm):
    class Meta:
        fields = ["text", "is_correct"]
        model = Answer


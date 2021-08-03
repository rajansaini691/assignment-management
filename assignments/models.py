from django.db import models
from django.utils.translation import gettext_lazy as _

class Assignment(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Question(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

class QuestionComponent(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class QuestionComponentTypes(models.TextChoices):
        VARIABLE = "V", _("Variable")
        TEXT = "T", _("Text")

    component_type = models.CharField(
            max_length=1,
            choices=QuestionComponentTypes.choices)

    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

# A multiple-choice answer
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.answer_text

from django.forms import ModelForm

from .models import AssignmentTemplate

class AssignmentTemplateForm(ModelForm):
    class Meta:
        fields = ["schema"]
        model = AssignmentTemplate

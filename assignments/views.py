from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.core import serializers

from .forms import AssignmentTemplateForm
from .models import AssignmentTemplate, Assignment

import json
import sympy
import random

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'assignments/index.html'
    context_object_name = 'latest_assignment_list'

    def get_queryset(self):
        return AssignmentTemplate.objects.order_by('-id')[:5]


def edit_assignment_template(request, pk):
    assignment_template = get_object_or_404(AssignmentTemplate, pk=pk)
    context = {
        'assignment_template_form': AssignmentTemplateForm(instance=assignment_template),
    }
    return render(request, 'assignments/edit_assignment.html', context)

def save_assignment_template(request, pk):
    assignment_template = get_object_or_404(AssignmentTemplate, pk=pk)
    assignment_template.schema = json.loads(request.POST['schema'])
    assignment_template.save()
    return HttpResponseRedirect(reverse('assignments:edit', args=(assignment_template.id,)))

# TODO This should probably go somewhere else
# Precondition - all inputs sanitized
def instantiate_assignment(template_schema):
    for problem in template_schema:
        # TODO rename answer to answers in schema
        # TODO rename choice to content in schema
        # TODO Substitute these guys back in (could also consider doing it in-place to ensure correctness)
        # TODO Write many tests for this, as it needs to be reliable
        symbols = [(sympy.Symbol(var['content']), random.randint(0, 50)) for var in problem['question'] if var['type'] == 'VAR']
        answers = [sympy.sympify(choice['choice']).subs(symbols) for choice in problem['answer']]
    return template_schema

def generate_assignments(request, pk):
    # Retrieve the assignment template corresponding to the pk and give it n assignments
    assignment_template = get_object_or_404(AssignmentTemplate, pk=pk)
    n = int(request.POST['num_assignments'])

    assignment_template.assignment_set.all().delete()

    # FIXME Need to sanitize input to avoid vulnerabilities
    for i in range(n):
        instantiated_schema = instantiate_assignment(assignment_template.schema)
        assignment = Assignment(template=assignment_template, schema=instantiated_schema)
        assignment.save()
    return HttpResponseRedirect(reverse('assignments:edit', args=(assignment_template.id,)))

def create_assignment_template(request):
    assignment_template = AssignmentTemplate(title=request.POST['title'], schema={'test': 'test'})
    assignment_template.save()
    return HttpResponseRedirect(reverse('assignments:edit', args=(assignment_template.id,)))

class AssignmentTemplateView(generic.DetailView):
    model = AssignmentTemplate
    template_name = 'assignments/view_template.html'

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .forms import AssignmentTemplateForm
from .models import AssignmentTemplate, Assignment

import json

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

def generate_assignments(request, pk):
    # Retrieve the assignment template corresponding to the pk and give it n assignments
    assignment_template = get_object_or_404(AssignmentTemplate, pk=pk)
    n = int(request.POST['num_assignments'])

    assignment_template.assignment_set.all().delete()

    for i in range(n):
        # TODO Each assignment should instantiate the symbols
        assignment = Assignment(template=assignment_template, schema=assignment_template.schema)
        assignment.save()
    return HttpResponseRedirect(reverse('assignments:edit', args=(assignment_template.id,)))

def create_assignment_template(request):
    assignment_template = AssignmentTemplate(title=request.POST['title'], schema={'test': 'test'})
    assignment_template.save()
    return HttpResponseRedirect(reverse('assignments:edit', args=(assignment_template.id,)))

class AssignmentTemplateView(generic.DetailView):
    model = AssignmentTemplate
    template_name = 'assignments/view_template.html'

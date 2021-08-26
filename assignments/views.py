from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .forms import AssignmentTemplateForm
from .models import AssignmentTemplate

import json

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'assignments/index.html'
    context_object_name = 'latest_assignment_list'

    def get_queryset(self):
        return AssignmentTemplate.objects.order_by('-id')[:5]


def edit_assignment(request, pk):
    assignment = get_object_or_404(AssignmentTemplate, pk=pk)
    context = {
        'assignment_template_form': AssignmentTemplateForm(instance=assignment),
    }
    return render(request, 'assignments/edit_assignment.html', context)

def save_assignment(request, pk):
    assignment = get_object_or_404(AssignmentTemplate, pk=pk)
    assignment.schema = json.loads(request.POST['schema'])
    assignment.save()
    return HttpResponseRedirect(reverse('assignments:edit', args=(assignment.id,)))


def create_assignment(request):
    assignment = AssignmentTemplate(title=request.POST['title'], schema={'test': 'test'})
    assignment.save()
    return HttpResponseRedirect(reverse('assignments:edit', args=(assignment.id,)))

class AssignmentTemplateView(generic.DetailView):
    model = AssignmentTemplate
    template_name = 'assignments/view_template.html'

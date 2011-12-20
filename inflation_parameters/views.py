from django.http import HttpResponse, HttpResponseRedirect
from inflation_parameters.models import ExpChoice, Expense, Identifier, IdfrChoice
from django.template import Context, loader, RequestContext, Template
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse

# views define templates and dictionaries, as well as direct the user if the
# site requested does not exist (404).

def detail(request, identifier_id):
    i = get_object_or_404(Identifier, pk=identifier_id)
    return render_to_response('/inflation_parameters/', {'identifier': i},
                              context_instance=RequestContext(request))
    
def results(request, identifier_id):
    i = get_object_or_404(Identifier, pk=identifier_id)
    return render_to_response('identifiers/results.html', {'identifier': i}, context_instance=RequestContext(request))
    
    
def home(request):
    return render_to_response('forms/wizard.html',
                              context_instance=RequestContext(request))

def documentation(request):
    return render_to_response('identifiers/documentation.html', context_instance=RequestContext(request))
    
def design(request):
    return render_to_response('identifiers/design.html', context_instance=RequestContext(request))
    
def calculations(request):
    return render_to_response('identifiers/calculations.html', context_instance=RequestContext(request))
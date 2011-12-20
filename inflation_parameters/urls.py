from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from inflation_parameters.models import Identifier
from inflation_parameters.forms import DemographicsForm, HousingForm, FoodForm
from inflation_parameters.forms import EntertainForm, UtilitiesForm, EducationForm
from inflation_parameters.forms import TransForm, ClothingForm, OtherForm
from inflation_parameters.forms import HealthForm, ParameterWizard


urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Identifier.objects.order_by('question'),
            context_object_name='latest_identifier_list',
            template_name='identifiers/index.html')),
    url(r'^(?P<pk>\d+)/$', ParameterWizard([DemographicsForm, HousingForm, FoodForm,
                                EntertainForm, UtilitiesForm, EducationForm,
                                TransForm, ClothingForm, HealthForm,
                                OtherForm])),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Identifier,
            template_name='identifiers/results.html'),
        name='identifier_results'),
)

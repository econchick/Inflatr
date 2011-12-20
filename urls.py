from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from inflation_parameters.models import Identifier
from inflation_parameters.forms import DemographicsForm, HousingForm, FoodForm
from inflation_parameters.forms import EntertainForm, UtilitiesForm, EducationForm
from inflation_parameters.forms import TransForm, ClothingForm, OtherForm
from inflation_parameters.forms import HealthForm, ParameterWizard
from django.contrib import admin

# URL paths as used in home.html
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^inflation_parameters/', include('inflation_parameters.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ParameterWizard([DemographicsForm, HousingForm, FoodForm,
                                TransForm, HealthForm, EntertainForm,
                                EducationForm, UtilitiesForm, ClothingForm,
                                OtherForm])),
    url(r'^documentation.html', 'inflation_parameters.views.documentation'),
    url(r'^design.html', 'inflation_parameters.views.design'),
    url(r'^calculations.html', 'inflation_parameters.views.calculations')
)

urlpatterns += staticfiles_urlpatterns()
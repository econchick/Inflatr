from django import forms
from django.forms import ModelForm
from inflation_parameters.models import Identifier, IdfrChoice, ExpChoice, Expense
from django.contrib.formtools.wizard import FormWizard
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from formulas import *
from django.template import RequestContext


# one class per page for the form.  feeds into wizard.html

# demographics/Identifier portion
class DemographicsForm(forms.Form):
    gender = forms.ModelChoiceField(queryset=IdfrChoice.objects.filter(identifier=1))
    age = forms.ModelChoiceField(queryset=IdfrChoice.objects.filter(identifier=2))
    region = forms.ModelChoiceField(queryset=IdfrChoice.objects.filter(identifier=3))
    salary = forms.ModelChoiceField(queryset=IdfrChoice.objects.filter(identifier=4))
    marital_status = forms.ModelChoiceField(queryset=IdfrChoice.objects.filter(identifier=6))
    dependents = forms.ModelChoiceField(queryset=IdfrChoice.objects.filter(identifier=5))

# expenses portions
class HousingForm(forms.Form):
    # Housing group = 1
    rent = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=1))
    own = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=2))
    free = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=3))
#    other = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=4))
    
class FoodForm(forms.Form):
    # Food & Dining group = 2
    groceries = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=5))
    dining_out = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=6))
    alcohol = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=7))

class TransForm(forms.Form): 
    # Transportation group = 3
    gas = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=8))
    payments_maintenance_and_traffic_tickets = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=30))
    public_transportation = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=9))
    human_powered_transportation = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=10))
    other = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=11))

class HealthForm(forms.Form):
    # health group = 4
    medical_dental_and_vision_out_of_pocket = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=12))
    personal_care_products = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=13))
    personal_care_services = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=14))

class EntertainForm(forms.Form):
    # entertainment group = 5
    recreation_and_entertainment = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=15))
    
class EducationForm(forms.Form):
    # education group = 6
    books = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=16))
    tuition = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=17))

class UtilitiesForm(forms.Form):   
    # utilities group = 7
    telephone_mobile_and_communications = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=18))
    internet_and_IT_services = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=19))
    electric_gas_and_energy = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=20))
    water_sewer_and_trash = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=21))
 
class ClothingForm(forms.Form):   
    # clothing group = 8
    clothing_for_self = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=22))
    clothing_for_female_dependents = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=23))
    clothing_for_male_dependents = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=24))
    footware_for_all = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=25))

class OtherForm(forms.Form):    
    # other group = 9
    tobacco_and_related_products = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=26))
    household_products_and_services = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=28))
    savings_and_investment = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=27))
    miscellanious = forms.ModelChoiceField(queryset=ExpChoice.objects.filter(expense=29))
 
 
# pulls form together, outputs to form_list/{{ results }} tag
# form_list is used in formulas.py, {{ results }} tag is used in
# results.html
class ParameterWizard(FormWizard):
    
    def done(self, request, form_list):
        return render_to_response('identifiers/results.html',
                                  {'results': personalized_inflation(form_list)},
                                  context_instance=RequestContext(request))


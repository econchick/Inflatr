from django.forms import ModelForm
from inflation_parameters.models import Identifier, IdfrChoice, ExpChoice, Expense

# one form class per page
# demographics portion
class Gender_Age(forms.ModelForm):
    class Meta:
        model = Identifier
        model = IdfrChoice

class Region(forms.ModelForm):
    class Meta:
        model = Identifier
        model = IdfrChoice

class Salary(forms.ModelForm):
    class Meta:
        model = Identifier
        model = IdfrChoice

class MaritalStatus_Dependents(forms.ModelForm):
    class Meta:
        model = Identifier
        model = IdfrChoice

# Expenses portion
class Housing(forms.ModelForm):
    class Meta:
        model = Expense
        model = ExpChoice

class FoodDining(forms.ModelForm):
    class Meta:
        model = Expense
        model = ExpChoice

class Clothing(forms.ModelForm):
    class Meta:
        model = Expense
        model = ExpChoice
        
class Transportation(forms.ModelForm):
    class Meta:
        model = Expense
        model = ExpChoice

class Health(forms.ModelForm):
    class Meta:
        model = Expense
        model = ExpChoice

class Education(forms.ModelForm):
    class Meta:
        model = Expense
        model = ExpChoice

class Entertainment(forms.ModelForm):
    class Meta:
        model = Expense
        model = ExpChoice
        
class Utilities(forms.ModelForm):
    class Meta:
        model = Expense
        model = ExpChoice

class Misc(forms.ModelForm):
    class Meta:
        model = Expense
        model = ExpChoice
        
class ParameterWizard(FormWizard):
    def done(self, request, form_list):
        return HttpResponseRedirect('/inflation_calc.html')
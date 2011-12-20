from inflation_parameters.models import Identifier, Expense, IdfrChoice, ExpChoice, InflationData
from django.contrib import admin

class IdfrChoiceInline(admin.TabularInline):
    model = IdfrChoice
    extra = 1

class IdentifierAdmin(admin.ModelAdmin):
    fields = ['question']
    inlines = [IdfrChoiceInline]
    list_display = ['question']

    
admin.site.register(Identifier, IdentifierAdmin)

class ExpChoiceInline(admin.TabularInline):
    model = ExpChoice
    extra = 1

class ExpenseAdmin(admin.ModelAdmin):
    fields = ['group', 'question']
    inlines = (ExpChoiceInline, )
    list_display = ('question', 'group')
    list_filter = ['group']
    
admin.site.register(Expense, ExpenseAdmin)

    
class InflationDataAdmin(admin.ModelAdmin):
    fields = ['series', 'area', 'year', 'frequency', 'pointinyear', 'value']
    list_display = ('series','area', 'year', 'frequency', 'pointinyear', 'value')
    list_filter = ['area']

admin.site.register(InflationData, InflationDataAdmin)
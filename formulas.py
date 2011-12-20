# this file defines the formula to calculate individual inflation
# based off of user input from {{ form }}in home.html and uploaded data
# from bls.gov at ftp://ftp.bls.gov/pub/time.series/cu/cu.data.0.Current
# data was parsed w/ parser.py, using area_names.py and items.py

from inflationdata.items import *
from inflationdata.area_names import *
from inflation_parameters.models import Expense, ExpChoice, Identifier, IdfrChoice, InflationData

# mode: monthly
mode = 12

# time period for calculations & graphing

all_years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]

# grabbing data from form input

def get_index(element, identifier):
    return list(IdfrChoice.objects.filter(identifier=identifier)).index(element)

# gender
def gender_calc(form_list):
    gender_index = get_index(form_list[0].cleaned_data['gender'], 1)
    gender_values = [0, 1]
    gender = gender_values[gender_index]
    
    return gender
    
# age
def age_calc(form_list):
    age_index = get_index(form_list[0].cleaned_data['age'], 2)
    age_values = [18, 22, 29, 59, 60]
    age = age_values[gender_index]
    
    return age

# region
def region_calc(form_list):
    region = form_list[0].cleaned_data['region'].idfrchoice
    
    return region

# salary
def salary_calc(form_list):
    salary_index = get_index(form_list[0].cleaned_data['salary'], 4)
    salary_values = [19999, 29999, 39999, 49999, 59999, 69999, 79999, 89999, 99999, 100000]
    salary = salary_values[salary_index]
    
    return salary
    
# dependents inflation calc
def dependent_calc(form_list):
    dep_index = get_index(form_list[0].cleaned_data['dependents'], 5)
    dependent_values = [0, 1, 2]
    dependents = dependent_values[dep_index]
    
    return dependents

# marital status
def marital_calc(form_list):
    marital_index = get_index(form_list[0].cleaned_data['marital_status'], 6)
    marital_values = [0, 1]
    marital = marital_values[marital_index]
    
    return marital

# expenses
    
def get_exp_index(element, expense):
    return list(ExpChoice.objects.filter(expense=expense)).index(element)
    
# housing
def rent_calc(form_list):
    rent_index = get_exp_index(form_list[1].cleaned_data['rent'], 1)
    rent_values = [0, 499, 749, 999, 1499, 1999, 2999, 3999, 4000]
    rent = rent_values[rent_index]
    
    return rent

def own_calc(form_list):
    own_index = get_exp_index(form_list[1].cleaned_data['own'], 2)
    own_values = [0, 499, 749, 999, 1499, 1999, 2999, 3999, 4000]
    own = own_values[own_index]
    
    return own

# if 1, then either rent or own, if 0, no shelter expenses
def free_calc(form_list):
    free_index = get_exp_index(form_list[1].cleaned_data['free'], 3)
    free_values = [0, 1]
    free = free_values[free_index]

# food
def groceries_calc(form_list):
    groceries_index = get_exp_index(form_list[2].cleaned_data['groceries'], 5)
    groceries_value = [0, 49, 99, 199, 299, 399, 499, 749, 999, 1000]
    groceries = groceries_value[groceries_index]
    
    return groceries

def diningout_calc(form_list):
    dining_index = get_exp_index(form_list[2].cleaned_data['dining_out'], 6)
    dining_value = [0, 49, 99, 199, 299, 399, 499, 749, 999, 1000]
    dining = dining_value[dining_index]
    
    return dining

def alcohol_calc(form_list):
    alcohol_index = get_exp_index(form_list[2].cleaned_data['alcohol'], 7)
    alcohol_value = [0, 49, 99, 199, 299, 300]
    alcohol = alcohol_value[alcohol_index]
    
    return alcohol

# transportation
def gas_calc(form_list):
    gas_index = get_exp_index(form_list[3].cleaned_data['gas'], 8)
    gas_value = [0, 19, 39, 59, 79, 99, 149, 199, 200]
    gas = gas_value[gas_index]
    
    return gas

def public_calc(form_list):
    public_index = get_exp_index(form_list[3].cleaned_data['public_transportation'], 9)
    public_value = [0, 19, 39, 59, 79, 99, 149, 199, 200]
    publictrans = public_value[public_index]
    
    return publictrans

def bike_calc(form_list):
    bike_index = get_exp_index(form_list[3].cleaned_data['human_powered_transportation'], 10)
    bike_value = [0, 19, 49, 50]
    bike = bike_value[bike_index]
    
    return bike

def payments_calc(form_list):
    payments_index = get_exp_index(form_list[3].cleaned_data['payments_maintenance_and_traffic_tickets'], 30)
    payments_value = [0, 99, 199, 299, 399, 499, 749, 999, 1000]
    payments = payments_value[payments_index]
    
    return payments

def other_trans_calc(form_list):
    other_index = get_exp_index(form_list[3].cleaned_data['other'], 11)
    other_value = [0, 99, 199, 200]
    other = other_value[other_index]
    
    return other

# health
def medical_calc(form_list):
    medical_index = get_exp_index(form_list[4].cleaned_data['medical_dental_and_vision_out_of_pocket'], 12)
    medical_value = [0, 99, 199, 299, 399, 499, 500]
    medical = medical_value[medical_index]
    
    return medical

def personalp_calc(form_list):
    personalp_index = get_exp_index(form_list[4].cleaned_data['personal_care_products'], 13)
    personalp_value = [0, 19, 39, 59, 79, 99, 100]
    personalp = personalp_value[personalp_index]
    
    return personalp

def personals_calc(form_list):
    personals_index = get_exp_index(form_list[4].cleaned_data['personal_care_services'], 14)
    personals_value = [0, 49, 99, 199, 200]
    personals = personals_value[personals_index]
    
    return personals

# recreation/entertainment
def rec_calc(form_list):
    rec_index = get_exp_index(form_list[5].cleaned_data['recreation_and_entertainment'], 15)
    rec_value = [0, 19, 49, 99, 199, 299, 749, 750]
    rec = rec_value[rec_index]
    
    return rec
    
# education
def books_calc(form_list):
    books_index = get_exp_index(form_list[6].cleaned_data['books'], 16)
    books_value = [0, 99, 199, 299, 300]
    books = books_value[books_index]
    
    return books

def tuition_calc(form_list):
    tuition_index = get_exp_index(form_list[6].cleaned_data['tuition'], 17)
    tuition_value = [0, 99, 499, 999, 1499, 1500]
    tuition = tuition_value[tuition_index]
    
    return tuition

# utilities
def telemobile_calc(form_list):
    telemobile_index = get_exp_index(form_list[7].cleaned_data['telephone_mobile_and_communications'], 18)
    telemobile_value = [0,49, 99, 149, 199, 200]
    telemobile = telemobile_value[telemobile_index]
    
    return telemobile

def internet_calc(form_list):
    internet_index = get_exp_index(form_list[7].cleaned_data['internet_and_IT_services'], 19)
    internet_value = [0, 49, 99, 149, 199, 200]
    internet = internet_value[internet_index]
    
    return internet

def energy_calc(form_list):
    energy_index = get_exp_index(form_list[7].cleaned_data['electric_gas_and_energy'], 20)
    energy_value = [0, 19, 49, 99, 199, 200]
    energy = energy_value[energy_index]
    
    return energy

def watersewer_calc(form_list):
    watersewer_index = get_exp_index(form_list[7].cleaned_data['water_sewer_and_trash'], 21)
    watersewer_value = [0, 19, 39, 59, 79, 99, 100]
    watersewer = watersewer_value[watersewer_index]
    
    return watersewer

# clothing
def clothingself_calc(form_list):
    clothingself_index = get_exp_index(form_list[8].cleaned_data['clothing_for_self'], 22)
    clothingself_value = [0, 49, 99, 199, 299, 300]
    clothingself = clothingself_value[clothingself_index]
    
    return clothingself

def clothing_female_calc(form_list):
    clothingfemale_index = get_exp_index(form_list[8].cleaned_data['clothing_for_female_dependents'], 23)
    clothingfemale_value = [0, 19, 39, 59, 79, 99, 100]
    clothingfemale = clothingfemale_value[clothingfemale_index]
    
    return clothingfemale

def clothing_male_calc(form_list):
    clothingmale_index = get_exp_index(form_list[8].cleaned_data['clothing_for_male_dependents'], 24)
    clothingmale_value = [0, 19, 39, 59, 79, 99, 100]
    clothingmale = clothingmale_value[clothingmale_index]
    
    return clothingmale

def footware_calc(form_list):
    footware_index = get_exp_index(form_list[8].cleaned_data['footware_for_all'], 25)
    footware_value = [0, 49, 99, 149, 299, 300]
    footware = footware_value[footware_index]
    
    return footware

# other
def tobacco_calc(form_list):
    tobacco_index = get_exp_index(form_list[9].cleaned_data['tobacco_and_related_products'], 26)
    tobacco_value = [0, 19, 49, 99, 199, 299, 300]
    tobacco = tobacco_value[tobacco_index]
    
    return tobacco

def household_calc(form_list):
    household_index = get_exp_index(form_list[9].cleaned_data['household_products_and_services'], 28)
    household_value = [0, 49, 99, 199, 299, 300]
    household = household_value[household_index]
    
    return household
    
def savings_calc(form_list):
    savings_index = get_exp_index(form_list[9].cleaned_data['savings_and_investment'], 27)
    savings_value = [0, .049, .099, .149, .249, .299, .3]
    savings = savings_value[savings_index]
    
    return savings

# $$ of savings
def calc_savings_salary(form_list):
    savings = savings_calc(form_list)
    year = salary_calc(form_list)
    salary = year/mode
    
    return savings*salary

def misc_calc(form_list):
    misc_index = get_exp_index(form_list[9].cleaned_data['miscellanious'], 29)
    misc_value = [0, 1]
    misc = misc_value[misc_index]
    
    return misc


def total_less_misc_calc(form_list):
    rent = rent_calc(form_list)
    own = own_calc(form_list)
    groceries = groceries_calc(form_list)
    diningout = diningout_calc(form_list)
    alcohol = alcohol_calc(form_list)
    gas = gas_calc(form_list)
    bike = bike_calc(form_list)
    publictrans = public_calc(form_list)
    other = other_trans_calc(form_list)
    medical = medical_calc(form_list)
    personalp = personalp_calc(form_list)
    personals = personals_calc(form_list)
    rec = rec_calc(form_list)
    books = books_calc(form_list)
    tuition = tuition_calc(form_list)
    telemobile = telemobile_calc(form_list)
    internet = internet_calc(form_list)
    energy = energy_calc(form_list)
    watersewer = watersewer_calc(form_list)
    clothingself = clothingself_calc(form_list)
    clothingfemale = clothing_female_calc(form_list)
    clothingmale = clothing_male_calc(form_list)
    footware = footware_calc(form_list)
    tobacco = tobacco_calc(form_list)
    household = household_calc(form_list)
    savings = calc_savings_salary(form_list)
    salary = salary_calc(form_list)/mode
    
    total = (rent+own+groceries+diningout+alcohol+gas+
             bike+publictrans+other+medical+personalp+
             personals+rec+books+tuition+telemobile+
             internet+energy+watersewer+clothingself+
             clothingfemale+clothingmale+footware+household+
             savings)
    
    return total
    
# catch all other unlisted expenses and allocate salary $
def calc_misc_salary(form_list):
    misc = misc_calc(form_list)
    year = salary_calc(form_list)
    salary = year/mode
    
    if (misc == 1):
        salary = salary_calc(form_list)/mode       
        total = total_less_misc_calc(form_list)
        
        remaining = (salary - total)
        
        if (remaining <= 0):
            misc_remain = 0
        else:
            misc_remain = remaining
            
    else:
        misc_remain = 0
    
    return misc_remain

# rebalance if total > salary
def rebalance_calc(form_list):
    savings = calc_savings_salary(form_list)
    salary = (salary_calc(form_list)/mode)-savings
    total_wo_misc = total_less_misc_calc(form_list)
    total = total_wo_misc + calc_misc_salary(form_list)
  
    if (total != salary): # total should be greater/equal to salary by now anyways
        salary = total

    return salary

# grab appropriate inflation calculations
def rent_inflation1(form_list, start_year, end_year):
    rent = rent_calc(form_list)
    region = region_calc(form_list)
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_rent1 = InflationData.objects.filter(area=region,
                                             series="Rent of primary residence",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_rent2 = InflationData.objects.filter(area=region,
                                             series="Rent of primary residence",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    
    inflation1 = (bls_rent2-bls_rent1)/(bls_rent1)
    weight = rent/rebalance_calc(form_list)
    
    return inflation1*weight
    
def own_inflation1(form_list, start_year, end_year):
    own = own_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_own1 = InflationData.objects.filter(area=region,
                                             series="Owners\' equivalent rent of residences",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_own2 = InflationData.objects.filter(area=region,
                                             series="Owners\' equivalent rent of residences",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    inflation1 = (bls_own2-bls_own1)/bls_own2
    weight = own/rebalance_calc(form_list)
    
    return inflation1*weight
       
def groceries_inflation1(form_list, start_year, end_year):
    groceries = groceries_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_groceries1 = InflationData.objects.filter(area=region,
                                             series="Food at home",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_groceries2 = InflationData.objects.filter(area=region,
                                             series="Food at home",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    inflation1 = (bls_groceries2-bls_groceries1)/bls_groceries2
    weight = groceries/rebalance_calc(form_list)
    
    return inflation1*weight
    
def diningout_inflation1(form_list, start_year, end_year):
    diningout = diningout_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_diningout1 = InflationData.objects.filter(area=region,
                                             series="Food away from home",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_diningout2 = InflationData.objects.filter(area=region,
                                             series="Food away from home",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    inflation1 = (bls_diningout2-bls_diningout1)/bls_diningout2
    weight = diningout/rebalance_calc(form_list)
    
    return inflation1*weight
    
def alcohol_inflation1(form_list, start_year, end_year):
    alcohol = alcohol_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_alcohol1 = InflationData.objects.filter(area=region,
                                             series="Alcoholic beverages",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_alcohol2 = InflationData.objects.filter(area=region,
                                             series="Alcoholic beverages",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_alcohol2-bls_alcohol1)/bls_alcohol2
    weight = alcohol/rebalance_calc(form_list)
    
    return inflation1*weight
    
def gas_inflation1(form_list, start_year, end_year):
    gas = gas_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_gas1 = InflationData.objects.filter(area=region,
                                             series="Motor fuel",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_gas2 = InflationData.objects.filter(area=region,
                                             series="Motor fuel",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_gas2-bls_gas1)/bls_gas2
    weight = gas/rebalance_calc(form_list)
    
    return inflation1*weight
    
def publictrans_inflation1(form_list, start_year, end_year):
    publictrans = public_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_publictrans1 = InflationData.objects.filter(area=region,
                                             series="Transportation",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_publictrans2 = InflationData.objects.filter(area=region,
                                             series="Transportation",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_publictrans2-bls_publictrans1)/bls_publictrans2
    weight = publictrans/rebalance_calc(form_list)
    
    return inflation1*weight
    
def bike_inflation1(form_list, start_year, end_year):
    bike = bike_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_bike1 = InflationData.objects.filter(area=region,
                                             series="Sporting goods",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_bike2 = InflationData.objects.filter(area=region,
                                             series="Sporting goods",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_bike2-bls_bike1)/bls_bike2
    weight = bike/rebalance_calc(form_list)
    
    return inflation1*weight
    
def other_inflation1(form_list, start_year, end_year):
    other = other_trans_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_other1 = InflationData.objects.filter(area=region,
                                             series="Transportation",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_other2 = InflationData.objects.filter(area=region,
                                             series="Transportation",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_other2-bls_other1)/bls_other2
    weight = other/rebalance_calc(form_list)
    
    return inflation1*weight
        
def payments_inflation1(form_list, start_year, end_year):
    payments = payments_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"

    bls_payments1 = InflationData.objects.filter(area=region,
                                             series="Transportation",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_payments2 = InflationData.objects.filter(area=region,
                                             series="Transportation",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value
    

    inflation1 = (bls_payments2-bls_payments1)/bls_payments2
    weight = payments/rebalance_calc(form_list)
    
    return inflation1*weight
        
def medical_inflation1(form_list, start_year, end_year):
    medical = medical_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_medical1 = InflationData.objects.filter(area=region,
                                             series="Medical care",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_medical2 = InflationData.objects.filter(area=region,
                                             series="Medical care",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value


    inflation1 = (bls_medical2-bls_medical1)/bls_medical2
    weight = medical/rebalance_calc(form_list)
    
    return inflation1*weight
        
def personalp_inflation1(form_list, start_year, end_year):
    personalp = personalp_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_personalp1 = InflationData.objects.filter(area=region,
                                             series="Medical care",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_personalp2 = InflationData.objects.filter(area=region,
                                             series="Medical care",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_personalp2-bls_personalp1)/bls_personalp2
    weight = personalp/rebalance_calc(form_list)
    
    return inflation1*weight
        
def personals_inflation1(form_list, start_year, end_year):
    personals = personals_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_personals1 = InflationData.objects.filter(area=region,
                                             series="Services",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_personals2 = InflationData.objects.filter(area=region,
                                             series="Services",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_personals2-bls_personals1)/bls_personals2
    weight = personals/rebalance_calc(form_list)
    
    return inflation1*weight

# recreation & entertainment
def rec_inflation1(form_list, start_year, end_year):
    rec = rec_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_rec1 = InflationData.objects.filter(area=region,
                                             series="Recreation",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_rec2 = InflationData.objects.filter(area=region,
                                             series="Recreation",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    inflation1 = (bls_rec2-bls_rec1)/bls_rec2
    weight = rec/rebalance_calc(form_list)
    
    return inflation1*weight

# education    
def books_inflation1(form_list, start_year, end_year):
    books = books_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_books1 = InflationData.objects.filter(area=region,
                                             series="Education and communication",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_books2 = InflationData.objects.filter(area=region,
                                             series="Education and communication",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_books2-bls_books1)/bls_books2
    weight = books/rebalance_calc(form_list)
    
    return inflation1*weight
        
def tuition_inflation1(form_list, start_year, end_year):
    tuition = tuition_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_tuition1 = InflationData.objects.filter(area=region,
                                             series="Education and communication",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_tuition2 = InflationData.objects.filter(area=region,
                                             series="Education and communication",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_tuition2-bls_tuition1)/bls_tuition2
    weight = tuition/rebalance_calc(form_list)
    
    return inflation1*weight
    
    
# utilities
def telemobile_inflation1(form_list, start_year, end_year):
    telemobile = telemobile_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_telemobile1 = InflationData.objects.filter(area=region,
                                             series="Education and communication",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_telemobile2 = InflationData.objects.filter(area=region,
                                             series="Education and communication",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_telemobile2-bls_telemobile1)/bls_telemobile2
    weight = telemobile/rebalance_calc(form_list)
    
    return inflation1*weight
      
def internet_inflation1(form_list, start_year, end_year):
    internet = internet_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_internet1 = InflationData.objects.filter(area=region,
                                             series="Education and communication",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_internet2 = InflationData.objects.filter(area=region,
                                             series="Education and communication",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_internet2-bls_internet1)/bls_internet2
    weight = internet/rebalance_calc(form_list)
    
    return inflation1*weight

    
def energy_inflation1(form_list, start_year, end_year):
    energy = energy_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_energy1 = InflationData.objects.filter(area=region,
                                             series="Energy",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_energy2 = InflationData.objects.filter(area=region,
                                             series="Energy",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_energy2-bls_energy1)/bls_energy2
    weight = energy/rebalance_calc(form_list)
    
    return inflation1*weight
        
def watersewer_inflation1(form_list, start_year, end_year):
    watersewer = watersewer_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_watersewer1 = InflationData.objects.filter(area=region,
                                             series="Fuels and utilities",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_watersewer2 = InflationData.objects.filter(area=region,
                                             series="Fuels and utilities",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_watersewer2-bls_watersewer1)/bls_watersewer2
    weight = watersewer/rebalance_calc(form_list)
    
    return inflation1*weight    
    
def clothingself_inflation1(form_list, start_year, end_year):
    clothingself = clothingself_calc(form_list)
    region = region_calc(form_list)
    gender = gender_calc(form_list)
    
  
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
        
        
    if (gender == 0): # female
        bls_clothingself1 = InflationData.objects.filter(area=region,
                                                 series="Apparel",
                                                 year=start_year, frequency=freq,
                                                 pointinyear=period)[0].value
        
        bls_clothingself2 = InflationData.objects.filter(area=region,
                                                 series="Apparel",
                                                 year=end_year, frequency=freq,
                                                 pointinyear=period)[0].value
    
    else: # male
        bls_clothingself1 = InflationData.objects.filter(area=region,
                                                 series="Apparel",
                                                 year=start_year, frequency=freq,
                                                 pointinyear=period)[0].value
        
        bls_clothingself2 = InflationData.objects.filter(area=region,
                                                 series="Apparel",
                                                 year=end_year, frequency=freq,
                                                 pointinyear=period)[0].value

    
    inflation1 = (bls_clothingself2-bls_clothingself1)/bls_clothingself2
    weight = clothingself/rebalance_calc(form_list)
    
    return inflation1*weight
       
def clothing_female_inflation1(form_list, start_year, end_year):
    clothingfemale = clothing_female_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_clothingfemale1 = InflationData.objects.filter(area=region,
                                             series="Apparel",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_clothingfemale2 = InflationData.objects.filter(area=region,
                                             series="Apparel",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_clothingfemale2-bls_clothingfemale1)/bls_clothingfemale2
    weight = clothingfemale/rebalance_calc(form_list)
    
    return inflation1*weight

def clothing_male_inflation1(form_list, start_year, end_year):
    clothingmale = clothing_male_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_clothingmale1 = InflationData.objects.filter(area=region,
                                             series="Apparel",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_clothingmale2 = InflationData.objects.filter(area=region,
                                             series="Apparel",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_clothingmale2-bls_clothingmale1)/bls_clothingmale2
    weight = clothingmale/rebalance_calc(form_list)
    
    return inflation1*weight
       
def footware_inflation1(form_list, start_year, end_year):
    footware = footware_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_footware1 = InflationData.objects.filter(area=region,
                                             series="Apparel",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_footware2 = InflationData.objects.filter(area=region,
                                             series="Apparel",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_footware2-bls_footware1)/bls_footware2
    weight = footware/rebalance_calc(form_list)
    
    return inflation1*weight
    
# other    
def tobacco_inflation1(form_list, start_year, end_year):
    tobacco = tobacco_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_tobacco1 = InflationData.objects.filter(area=region,
                                             series="Other goods and services",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_tobacco2 = InflationData.objects.filter(area=region,
                                             series="Other goods and services",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_tobacco2-bls_tobacco1)/bls_tobacco2
    weight = tobacco/rebalance_calc(form_list)
    
    return inflation1*weight
     
def household_inflation1(form_list, start_year, end_year):
    household = household_calc(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_household1 = InflationData.objects.filter(area=region,
                                             series="Household furnishings and operations",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_household2 = InflationData.objects.filter(area=region,
                                             series="Household furnishings and operations",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_household2-bls_household1)/bls_household2
    weight = household/rebalance_calc(form_list)
    
    return inflation1*weight
        
def misc_inflation1(form_list, start_year, end_year):
    misc = calc_misc_salary(form_list)
    region = region_calc(form_list)
    
    
    # These areas are only reported Semiannually, so frequency has to be limited
    # as such.  All others are reported monthly, or every other month but still
    # contain data for every month.  Point in year(=period) is dependent on
    # frequency, where "03" = end of the year for semiannually, and "13" = end
    # of the year for monthly
    if (region == "Anchorage AK" or region == "Cincinnati-Hamilton OH-KY-IN"
        or region == "Denver-Boulder-Greeley CO" or region == "Honolulu HI"
        or region == "Kansas City MO-KS" or region == "Milwaukee-Racine WI"
        or region == "Minneapolis-St. Paul MN-WI" or region == "Pitsburgh PA"
        or region == "Portland-Salem OR-WA" or region == "St. Louis MO-IL"
        or region == "San Diego CA" or region == "Tampa-St. Petersburg-Clearwater FL"):
        
        freq="S"
        period="03"
    else:
        freq="M"
        period="13"
    
    bls_misc1 = InflationData.objects.filter(area=region,
                                             series="All items less food and energy",
                                             year=start_year, frequency=freq,
                                             pointinyear=period)[0].value
    
    bls_misc2 = InflationData.objects.filter(area=region,
                                             series="All items less food and energy",
                                             year=end_year, frequency=freq,
                                             pointinyear=period)[0].value

    
    inflation1 = (bls_misc2-bls_misc1)/bls_misc2
    weight = misc/rebalance_calc(form_list)
    
    return inflation1*weight
    
def personalized_inflationX(form_list, start_year, end_year):
    return 100*(rent_inflation1(form_list, start_year, end_year)+own_inflation1(form_list, start_year, end_year)+
                               groceries_inflation1(form_list, start_year, end_year)+diningout_inflation1(form_list, start_year, end_year)+
                               alcohol_inflation1(form_list, start_year, end_year)+gas_inflation1(form_list, start_year, end_year)+
                               publictrans_inflation1(form_list, start_year, end_year)+payments_inflation1(form_list, start_year, end_year)+
                               medical_inflation1(form_list, start_year, end_year)+personalp_inflation1(form_list, start_year, end_year)+
                               personals_inflation1(form_list, start_year, end_year)+rec_inflation1(form_list, start_year, end_year)+
                               books_inflation1(form_list, start_year, end_year)+tuition_inflation1(form_list, start_year, end_year)+
                               telemobile_inflation1(form_list, start_year, end_year)+internet_inflation1(form_list, start_year, end_year)+
                               energy_inflation1(form_list, start_year, end_year)+watersewer_inflation1(form_list, start_year, end_year)+
                               clothingself_inflation1(form_list, start_year, end_year)+clothing_female_inflation1(form_list, start_year, end_year)+
                               clothing_male_inflation1(form_list, start_year, end_year)+footware_inflation1(form_list, start_year, end_year)+
                               tobacco_inflation1(form_list, start_year, end_year)+household_inflation1(form_list, start_year, end_year)+
                               misc_inflation1(form_list, start_year, end_year))
    
def personalized_inflation(form_list):
    return map(lambda start_year : personalized_inflationX(form_list, start_year, start_year + 1), all_years[0:len(all_years)-2])

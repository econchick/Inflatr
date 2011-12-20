from django.db import models

class Identifier(models.Model):
    question = models.CharField(max_length=200)
    def __unicode__(self):
        return self.question
    #pub_date = models.DateTimeField('date published')

class IdfrChoice(models.Model):
    identifier = models.ForeignKey(Identifier)
    idfrchoice = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
        return self.idfrchoice

class Expense(models.Model):
    question = models.CharField(max_length=200)
    group = models.CharField(max_length=200) # group of questions
    def __unicode__(self):
        return self.question
    
class ExpChoice(models.Model):
    expense = models.ForeignKey(Expense)
    expchoice = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
        return self.expchoice

class InflationData(models.Model):
    series = models.CharField(max_length=75)
    area = models.CharField(max_length=75)
    year = models.IntegerField()
    frequency = models.CharField(max_length=2)
    pointinyear = models.IntegerField()
    value = models.IntegerField()
    def __unicode__(self):
        return self.series
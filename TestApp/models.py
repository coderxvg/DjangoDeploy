from django.db import models

# Create your models here.
class TestTable(models.Model):
    id = models.AutoField(primary_key=True)
    Requestor = models.CharField(max_length=100)
    Role = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    StartDate =  models.CharField(max_length=100)
    Impact = models.CharField(max_length=100)
    DueDate = models.CharField(max_length=100)
    Scope = models.CharField(max_length=100)
    Notes = models.CharField(max_length=100)
    ProposedChange = models.CharField(max_length=100)
    Reson = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    ActionPlan = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    createdDate = models.CharField(max_length=100)


class Requestor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)


class Action(models.Model):
    id = models.AutoField(primary_key=True)
    Action = models.CharField(max_length=100)
    createdDate = models.CharField(max_length=100)
    Assignee = models.CharField(max_length=100)      
    
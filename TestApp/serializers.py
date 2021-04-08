from rest_framework import serializers
from .models import TestTable , Action


class CcrFormSerializer(serializers.Serializer):
    Requestor = serializers.CharField(max_length=100)
    Role = serializers.CharField(max_length=100)
    Department = serializers.CharField(max_length=100)
    StartDate =  serializers.CharField(max_length=100)
    Impact = serializers.CharField(max_length=100)
    DueDate = serializers.CharField(max_length=100)
    Scope = serializers.CharField(max_length=100)
    Notes = serializers.CharField(max_length=100)
    ProposedChange = serializers.CharField(max_length=100)
    Reson = serializers.CharField(max_length=100)
    Description = serializers.CharField(max_length=100)
    ActionPlan = serializers.CharField(max_length=100)
    Title = serializers.CharField(max_length=100)
    createdDate = serializers.CharField(max_length=100)
    id = serializers.IntegerField(read_only=True)

    def create(self, validate_data):
        return TestTable.objects.create(**validate_data)

class RequestorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    role = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=100)
    id = serializers.IntegerField(read_only=True)

class ActionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Action = serializers.CharField(max_length=100)
    createdDate = serializers.CharField(max_length=100)
    Assignee = serializers.CharField(max_length=100)    
    
    def create(self, validate_data):
        return Action.objects.create(**validate_data)

from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'eid': 'EMPLOYEE ID',
            'name': 'EMPLOYEE NAME',
            'designation': 'EMPLOYEE DESIGNATION',
        }
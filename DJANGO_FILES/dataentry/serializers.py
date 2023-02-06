from rest_framework import serializers
from dataentry.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        
class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'
        
class AadharSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aadhar
        fields = '__all__'
        
class FeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fees
        fields = '__all__'
        
class DepartmentCourseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departmentcourseinfo
        fields = '__all__'
        
class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departmentlist
        fields = '__all__'
        
class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = '__all__'
        
class ImpInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpInfo
        fields = '__all__'
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacherslist
        fields = '__all__'

class BacklogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backlogs
        fields = '__all__'
from rest_framework import serializers
from .models import *
from .models import CustomUser
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'
        
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email','password','first_name','last_name','username']
            
class AddStaffFormSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    address = serializers.CharField()
    admin_id = serializers.CharField()
    def create(self, validated_data):
        CustomUser_data = {
            'email': validated_data['email'],
            'password': validated_data['password'],
            'first_name': validated_data['first_name'],
            'last_name': validated_data['last_name'],
            'username': validated_data['username'],                    
        }
        Staff_data = {
            'address': validated_data['address'],
            'admin_id':validated_data['admin_id'],
        }
        CustomUser1 = CustomUser.objects.create(**CustomUser_data)
        Staff1 = Staff.objects.create(**Staff_data)
        return {'CustomUser': CustomUser1, 'Staff': Staff1}
    
class AddStudentFormSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    address = serializers.CharField()
    course = serializers.CharField()
    gender = serializers.CharField()
    session_start_year = serializers.CharField()
    session_end_year = serializers.CharField()
    admin_id = serializers.CharField()
    
    def create(self, validated_data):
        CustomUser_data = {
            'email': validated_data['email'],
            'password': validated_data['password'],
            'first_name': validated_data['first_name'],
            'last_name': validated_data['last_name'],
            'username': validated_data['username'],        
        }
        Students_data = {
            'gender': validated_data['gender'],
            'address': validated_data['address'],
            'session_start_year':validated_data['session_start_year'],
            'course_id_id':validated_data['course'],
            'session_end_year':validated_data['session_end_year'],
            'admin_id':validated_data['admin_id'],
        }
        CustomUser1 = CustomUser.objects.create(**CustomUser_data)
        Students1 = Students.objects.create(**Students_data)
        return {'CustomUser': CustomUser1, 'Students': Students1}
    
class AddSubjectFormSerializer(serializers.Serializer):
    subject_name = serializers.CharField()
    course = serializers.CharField()
    staff_id = serializers.CharField()
    subject_code = serializers.CharField()
    def create(self, validated_data):
        Subjects_data = {
            'subject_name': validated_data['subject_name'],
            'course_id_id': validated_data['course'],
            'staff_id_id': validated_data['staff_id'],
            'subject_code':validated_data['subject_code'],
        }
        Subjects1 = Subjects.objects.create(**Subjects_data)
        return {'Subjects': Subjects1}
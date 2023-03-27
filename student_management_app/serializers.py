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
        fields = '__all__'
        
        
class AddStaffFormSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    address = serializers.CharField()
    

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

        }
        CustomUser1 = CustomUser.objects.create(**CustomUser_data)
        Staff1 = Staff.objects.create(**Staff_data)
        return {'CustomUser': CustomUser1, 'Staff': Staff1}
        


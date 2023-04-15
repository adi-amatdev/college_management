from rest_framework import serializers
from .models import *
from .models import CustomUser

        
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
        fields = ('id','email','password','first_name','last_name','username','user_type','is_staff')
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.save()
        return instance
    
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'admin', 'address', 'created_at', 'updated_at')
    def update(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
    
class SessionYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionYearModel
        fields = ['session_start_year','session_end_year']
            
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
            'user_type': 2,
            'is_staff': 1,
        }
        Staff_data = {
            'address': validated_data['address'],
            'admin_id': validated_data['admin_id'],
        }
        CustomUser1 = CustomUser.objects.create(**CustomUser_data)
        CustomUser1.set_password(validated_data['password']) 
        CustomUser1.save()
        Staff1 = Staff.objects.create(admin=CustomUser1, **Staff_data)
        Staff1.save()
        return {'CustomUser': CustomUserSerializer(CustomUser1).data, 'Staff': StaffSerializer(Staff1).data}

    
class AddStudentFormSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    address = serializers.CharField()
    course_id = serializers.CharField()
    gender = serializers.CharField()
    #session_start_year = serializers.CharField()
    #session_end_year = serializers.CharField()
    #session_year_id = serializers.CharField()
    admin_id = serializers.CharField()
    
    def create(self, validated_data):
        CustomUser_data = {
            'email': validated_data['email'],
            'password': validated_data['password'],
            'first_name': validated_data['first_name'],
            'last_name': validated_data['last_name'],
            'username': validated_data['username'], 
            'user_type':3,       
        }
        Students_data = {
            'address': validated_data['address'],
            'gender': validated_data['gender'],
            'session_year_id_id':validated_data['session_year_id'],
            'course_id':validated_data['course_name'],
            'admin_id':validated_data['admin_id'],
        }
        CustomUser1 = CustomUser.objects.create(**CustomUser_data)
        CustomUser1.set_password(validated_data['password']) 
        CustomUser1.save()
        Students1 = Students.objects.create(**Students_data)
        Students1.save()
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
        
class UpdateStaffFormSerializer(serializers.Serializer):
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    address = serializers.CharField()

    def update(self, instance, validated_data):
        custom_user_instance = instance.admin
        custom_user_data = {
            'email': validated_data.get('email', custom_user_instance.email),
            'first_name': validated_data.get('first_name', custom_user_instance.first_name),
            'last_name': validated_data.get('last_name', custom_user_instance.last_name),
            'username': validated_data.get('username', custom_user_instance.username),
        }
        staff_data = {
            'address': validated_data.get('address', instance.address),
            'admin_id':validated_data.get('admin_id',instance.admin_id)
        }

        # update CustomUser fields
        for key, value in custom_user_data.items():
            setattr(custom_user_instance, key, value)

        # update Staff fields
        for key, value in staff_data.items():
            setattr(instance, key, value)

        custom_user_instance.save()
        instance.save()

        return {'CustomUser': custom_user_instance, 'Staff': instance}

    
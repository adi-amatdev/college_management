import pandas as pd
from django.db import models
from django.contrib.auth.models import AbstractUser


class SessionYearModel(models.Model):
    id = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    objects=models.Manager()

class CustomUser(AbstractUser):
    user_type_data = ((1,"AdminHOD"),(2,"Staff"),(3,"Student"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)


class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()
    
class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=255,blank=True)
    address = models.CharField(max_length=500,blank=True)
    objects=models.Manager()

class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=255,blank=True)
    department = models.ForeignKey(Courses,on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager() 
    
    
class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    sem = models.IntegerField(default=0)
    course_id = models.ForeignKey(Courses,on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=10,unique=True)
    staff_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()
    
    def __str__(self):
        return self.subject_code

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    gender = models.CharField(max_length=255)
    section = models.CharField(max_length=2,default='A')
    profile_pic = models.FileField()
    father_name = models.CharField(max_length=100,blank=True,null=True)
    father_num = models.BigIntegerField(default=0)
    mother_name = models.CharField(max_length=100,blank=True,null=True)
    mother_num = models.BigIntegerField(default=0)
    gaurdian_name=models.CharField(max_length=100,blank=True,null=True)
    gaurdian_num = models.BigIntegerField(blank=True,null=True)
    parent_or_gaurdian_email = models.EmailField(max_length=100,blank=True,null=True)
    address = models.TextField()
    objects=models.Manager()
    course_id = models.ForeignKey(Courses,on_delete=models.CASCADE,default=1)
    session_year_id = models.ForeignKey(SessionYearModel,on_delete=models.CASCADE,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class StudentLeave(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=60)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0) #  0 for pending , 1 for approved , 2 for rejected
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager() 
    
class StaffLeave(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=60)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager() 
    

class FeedbackStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager() 
    
class FeedbackStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager() 
    
class NotificationStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager()     

    
class NotificationStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=models.Manager() 

class TestDetails(models.Model):
    id = models.AutoField(primary_key=True)
    subject_code = models.ForeignKey(Subjects, on_delete=models.CASCADE,null = True)
    semester = models.IntegerField()
    test1_date = models.DateField()
    test2_date = models.DateField()
    test3_date = models.DateField()
    
    class Meta:
        unique_together = ('subject_code', 'semester')
    
class TestScores(models.Model):
    id = models.AutoField(primary_key=True)
    subject_code = models.ForeignKey(Subjects, on_delete=models.CASCADE,to_field='subject_code')
    usn = models.ForeignKey(CustomUser,on_delete = models.CASCADE,to_field ='username',null =  True)
    test1 = models.FloatField(default = '0.0')
    test2 = models.FloatField(default = '0.0')
    test3 = models.FloatField(default = '0.0')
    final = models.FloatField(default = '0.0')
    attendance = models.FloatField(default = '0.0')

    #removes the composite key problem , allowing constraints in combinations
    class Meta:
        unique_together = ('subject_code', 'usn')



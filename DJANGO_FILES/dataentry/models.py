# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aadhar(models.Model):
    aadhar_no = models.BigIntegerField(db_column='AADHAR_NO', primary_key=True)  # Field name made lowercase.
    usn = models.ForeignKey('Student', db_column='USN',on_delete=models.CASCADE,default=None)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aadhar'


class Attendance(models.Model):
    slno = models.IntegerField(db_column='SLNO', primary_key=True)  # Field name made lowercase.
    usn = models.ForeignKey('Student',db_column='USN',on_delete=models.CASCADE,default=None)  # Field name made lowercase.
    sub_code = models.ForeignKey('Departmentcourseinfo',db_column='SUB_CODE',on_delete=models.CASCADE,default=None)  # Field name made lowercase.
    classes_attended = models.IntegerField(db_column='CLASSES_ATTENDED', blank=True, null=True)  # Field name made lowercase.
    total_classes = models.IntegerField(db_column='TOTAL_CLASSES', blank=True, null=True)  # Field name made lowercase.
    percentage = models.DecimalField(db_column='PERCENTAGE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attendance'
        unique_together = (('slno', 'usn', 'sub_code'),)


class Backlogs(models.Model):
    slno = models.IntegerField(db_column='SLNO', primary_key=True)  # Field name made lowercase.
    usn = models.ForeignKey('Student',db_column='USN',on_delete=models.CASCADE,default=None)  # Field name made lowercase.
    backlogs_sub_code = models.CharField(db_column='BACKLOGS_SUB_CODE', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'backlogs'
        unique_together = (('slno', 'usn', 'backlogs_sub_code'),)


class Departmentcourseinfo(models.Model):
    dept = models.ForeignKey('Departmentlist',db_column='DEPT_ID', blank=True, null=True,on_delete=models.CASCADE,default=None)  # Field name made lowercase.
    subcode = models.CharField(db_column='SUBCODE', primary_key=True, max_length=10)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SUBJECTNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    no_of_credits = models.IntegerField(db_column='NO_OF_CREDITS', blank=True, null=True)  # Field name made lowercase.
    no_of_hours_per_week = models.IntegerField(db_column='NO_OF_HOURS_PER_WEEK', blank=True, null=True)  # Field name made lowercase.
    total_no_of_contact_hours = models.IntegerField(db_column='TOTAL_NO_OF_CONTACT_HOURS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departmentcourseinfo'


class Departmentlist(models.Model):
    dept_name = models.CharField(db_column='DEPT_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dept_id = models.CharField(db_column='DEPT_ID', primary_key=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departmentlist'


class Fees(models.Model):
    usn = models.OneToOneField('Student',db_column='USN', primary_key=True,on_delete=models.CASCADE,default=None)  # Field name made lowercase.
    college_fee = models.IntegerField(db_column='COLLEGE_FEE', blank=True, null=True)  # Field name made lowercase.
    hostel_fee = models.IntegerField(db_column='HOSTEL_FEE', blank=True, null=True)  # Field name made lowercase.
    library_fines = models.IntegerField(db_column='LIBRARY_FINES', blank=True, null=True)  # Field name made lowercase.
    other_fines = models.IntegerField(db_column='OTHER_FINES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fees'


class Hostel(models.Model):
    usn = models.OneToOneField('Student',db_column='USN', primary_key=True,on_delete=models.CASCADE,default=None)  # Field name made lowercase.
    girls_or_boys_hostel = models.CharField(db_column='GIRLS_OR_BOYS_HOSTEL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    room_no = models.CharField(db_column='ROOM_NO', max_length=5)  # Field name made lowercase.
    block_name = models.CharField(db_column='BLOCK_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hostel'


class ImpInfo(models.Model):
    usn = models.ForeignKey('Student',db_column='USN',on_delete=models.CASCADE,default=None)  # Field name made lowercase.
    number_10th_percentage = models.BigIntegerField(db_column='10TH_PERCENTAGE', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_12th_percentage = models.BigIntegerField(db_column='12TH_PERCENTAGE', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    name_of_school_10th = models.CharField(db_column='NAME_OF_SCHOOL_10TH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name_of_college_12th = models.CharField(db_column='NAME_OF_COLLEGE_12TH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    board_of_education_10th = models.CharField(db_column='BOARD_OF_EDUCATION_10TH', max_length=10, blank=True, null=True)  # Field name made lowercase.
    board_of_education_12th = models.CharField(db_column='BOARD_OF_EDUCATION_12TH', max_length=10, blank=True, null=True)  # Field name made lowercase.
    year_of_passing_10th = models.IntegerField(db_column='YEAR_OF_PASSING_10TH', blank=True, null=True)  # Field name made lowercase.
    year_of_passing_12th = models.IntegerField(db_column='YEAR_OF_PASSING_12TH', blank=True, null=True)  # Field name made lowercase.
    education_gap = models.IntegerField(db_column='EDUCATION_GAP', blank=True, null=True)  # Field name made lowercase.
    admission_quota_name = models.CharField(db_column='ADMISSION_QUOTA_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rank_from_entrance = models.BigIntegerField(db_column='RANK_FROM_ENTRANCE', blank=True, null=True)  # Field name made lowercase.
    bank_name = models.CharField(db_column='BANK_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bank_account_no = models.BigIntegerField(db_column='BANK_ACCOUNT_NO', blank=True, null=True)  # Field name made lowercase.
    pan_no = models.BigIntegerField(db_column='PAN_NO', blank=True, null=True)  # Field name made lowercase.
    voter_id_no = models.BigIntegerField(db_column='VOTER_ID_NO', blank=True, null=True)  # Field name made lowercase.
    passport_no = models.BigIntegerField(db_column='PASSPORT_NO', blank=True, null=True)  # Field name made lowercase.
    linkedin_id = models.CharField(db_column='LINKEDIN_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    github_id = models.CharField(db_column='GITHUB_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    awards = models.CharField(db_column='AWARDS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    certificates = models.CharField(db_column='CERTIFICATES', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'imp_info'


class Marks(models.Model):
    slno = models.IntegerField(db_column='SLNO', primary_key=True)  # Field name made lowercase.
    usn = models.ForeignKey('Student',db_column='USN',on_delete=models.CASCADE,default=None)  # Field name made lowercase.
    semester = models.IntegerField(db_column='SEMESTER', blank=True, null=True)  # Field name made lowercase.
    subcode = models.ForeignKey(Departmentcourseinfo, models.DO_NOTHING, db_column='SUBCODE')  # Field name made lowercase.
    ia1_scores = models.IntegerField(db_column='IA1_SCORES', blank=True, null=True)  # Field name made lowercase.
    ia2_scores = models.IntegerField(db_column='IA2_SCORES', blank=True, null=True)  # Field name made lowercase.
    ia3_scores = models.IntegerField(db_column='IA3_SCORES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'marks'
        unique_together = (('slno', 'usn', 'subcode'),)


class Parent(models.Model):
    usn = models.OneToOneField('Student',db_column='USN', primary_key=True,on_delete=models.CASCADE,default=None)  # Field name made lowercase.
    parent_or_gaurdian = models.CharField(db_column='PARENT_OR_GAURDIAN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    father_occupation = models.CharField(db_column='FATHER_OCCUPATION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fphone_no = models.IntegerField(db_column='FPHONE_NO', blank=True, null=True)  # Field name made lowercase.
    femail_id = models.CharField(db_column='FEMAIL_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mname = models.CharField(db_column='MNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mother_occupation = models.CharField(db_column='MOTHER_OCCUPATION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mphone_no = models.IntegerField(db_column='MPHONE_NO', blank=True, null=True)  # Field name made lowercase.
    memail_id = models.CharField(db_column='MEMAIL_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parent'


class Student(models.Model):
    usn = models.CharField(db_column='USN', primary_key=True, max_length=10)  # Field name made lowercase.
    student_fname = models.CharField(db_column='STUDENT_FNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    student_lname = models.CharField(db_column='STUDENT_LNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=7, blank=True, null=True)  # Field name made lowercase.
    email_id = models.CharField(db_column='EMAIL_ID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    blood_group = models.CharField(db_column='BLOOD_GROUP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dept_name = models.CharField(db_column='DEPT_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cur_sem = models.IntegerField(db_column='CUR_SEM', blank=True, null=True)  # Field name made lowercase.
    current_address = models.CharField(db_column='CURRENT_ADDRESS', max_length=300, blank=True, null=True)  # Field name made lowercase.
    permanent_address = models.CharField(db_column='PERMANENT_ADDRESS', max_length=300, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    hostel_or_dayscholar = models.CharField(db_column='HOSTEL_OR_DAYSCHOLAR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    doc_return_status = models.IntegerField(db_column='DOC_RETURN_STATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'


class Teacherslist(models.Model):
    slno = models.IntegerField(db_column='SLNO', primary_key=True)  # Field name made lowercase.
    tid = models.CharField(db_column='TID', max_length=10)  # Field name made lowercase.
    tname = models.CharField(db_column='TNAME', max_length=50)  # Field name made lowercase.
    subcode = models.ForeignKey(Departmentcourseinfo,db_column='SUBCODE',on_delete=models.CASCADE,default=None)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teacherslist'
        unique_together = (('slno', 'tid', 'tname'),)

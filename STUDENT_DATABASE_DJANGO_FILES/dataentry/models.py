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
    stid = models.ForeignKey('Student', models.DO_NOTHING, db_column='STID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aadhar'


class Attendance(models.Model):
    stdid = models.OneToOneField('Student', models.DO_NOTHING, db_column='STDID', primary_key=True)  # Field name made lowercase.
    subcode1 = models.CharField(db_column='SUBCODE1', max_length=7)  # Field name made lowercase.
    classes_attended1 = models.IntegerField(db_column='CLASSES_ATTENDED1', blank=True, null=True)  # Field name made lowercase.
    total_no_of_classes1 = models.IntegerField(db_column='TOTAL_NO_OF_CLASSES1', blank=True, null=True)  # Field name made lowercase.
    subcode2 = models.CharField(db_column='SUBCODE2', max_length=7)  # Field name made lowercase.
    classes_attended2 = models.IntegerField(db_column='CLASSES_ATTENDED2', blank=True, null=True)  # Field name made lowercase.
    total_no_of_classes2 = models.IntegerField(db_column='TOTAL_NO_OF_CLASSES2', blank=True, null=True)  # Field name made lowercase.
    subcode3 = models.CharField(db_column='SUBCODE3', max_length=7)  # Field name made lowercase.
    classes_attended3 = models.IntegerField(db_column='CLASSES_ATTENDED3', blank=True, null=True)  # Field name made lowercase.
    total_no_of_classes3 = models.IntegerField(db_column='TOTAL_NO_OF_CLASSES3', blank=True, null=True)  # Field name made lowercase.
    subcode4 = models.CharField(db_column='SUBCODE4', max_length=7)  # Field name made lowercase.
    classes_attended4 = models.IntegerField(db_column='CLASSES_ATTENDED4', blank=True, null=True)  # Field name made lowercase.
    total_no_of_classes4 = models.IntegerField(db_column='TOTAL_NO_OF_CLASSES4', blank=True, null=True)  # Field name made lowercase.
    subcode5 = models.CharField(db_column='SUBCODE5', max_length=7)  # Field name made lowercase.
    classes_attended5 = models.IntegerField(db_column='CLASSES_ATTENDED5', blank=True, null=True)  # Field name made lowercase.
    total_no_of_classes5 = models.IntegerField(db_column='TOTAL_NO_OF_CLASSES5', blank=True, null=True)  # Field name made lowercase.
    subcode6 = models.CharField(db_column='SUBCODE6', max_length=7)  # Field name made lowercase.
    classes_attended6 = models.IntegerField(db_column='CLASSES_ATTENDED6', blank=True, null=True)  # Field name made lowercase.
    total_no_of_classes6 = models.IntegerField(db_column='TOTAL_NO_OF_CLASSES6', blank=True, null=True)  # Field name made lowercase.
    subcode7 = models.CharField(db_column='SUBCODE7', max_length=7)  # Field name made lowercase.
    classes_attended7 = models.IntegerField(db_column='CLASSES_ATTENDED7', blank=True, null=True)  # Field name made lowercase.
    total_no_of_classes7 = models.IntegerField(db_column='TOTAL_NO_OF_CLASSES7', blank=True, null=True)  # Field name made lowercase.
    subcode8 = models.CharField(db_column='SUBCODE8', max_length=7)  # Field name made lowercase.
    classes_attended8 = models.IntegerField(db_column='CLASSES_ATTENDED8', blank=True, null=True)  # Field name made lowercase.
    total_no_of_classes8 = models.IntegerField(db_column='TOTAL_NO_OF_CLASSES8', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attendance'


class Backlogs(models.Model):
    stdid = models.OneToOneField('Student', models.DO_NOTHING, db_column='STDID', primary_key=True)  # Field name made lowercase.
    backlogs_sub_code = models.CharField(db_column='BACKLOGS_SUB_CODE', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'backlogs'
        unique_together = (('stdid', 'backlogs_sub_code'),)


class Department(models.Model):
    dept_name = models.CharField(db_column='DEPT_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    subcode = models.CharField(db_column='SUBCODE', primary_key=True, max_length=10)  # Field name made lowercase.
    subjectname = models.TextField(db_column='SUBJECTNAME', blank=True, null=True)  # Field name made lowercase.
    no_of_credits = models.IntegerField(db_column='NO_OF_CREDITS', blank=True, null=True)  # Field name made lowercase.
    no_of_hours_per_week = models.IntegerField(db_column='NO_OF_HOURS_PER_WEEK', blank=True, null=True)  # Field name made lowercase.
    total_no_of_contact_hours = models.IntegerField(db_column='TOTAL_NO_OF_CONTACT_HOURS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'


class Fees(models.Model):
    stdid = models.OneToOneField('Student', models.DO_NOTHING, db_column='STDID', primary_key=True)  # Field name made lowercase.
    college_fee = models.IntegerField(db_column='COLLEGE_FEE')  # Field name made lowercase.
    hostel_fee = models.IntegerField(db_column='HOSTEL_FEE', blank=True, null=True)  # Field name made lowercase.
    library_fines = models.IntegerField(db_column='LIBRARY_FINES', blank=True, null=True)  # Field name made lowercase.
    other_fines = models.IntegerField(db_column='OTHER_FINES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fees'
        unique_together = (('stdid', 'college_fee'),)


class Hostel(models.Model):
    stdid = models.OneToOneField('Student', models.DO_NOTHING, db_column='STDID', primary_key=True)  # Field name made lowercase.
    girls_or_boys_hostel = models.CharField(db_column='GIRLS_OR_BOYS_HOSTEL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    room_no = models.CharField(db_column='ROOM_NO', max_length=5)  # Field name made lowercase.
    block_name = models.CharField(db_column='BLOCK_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hostel'
        unique_together = (('stdid', 'room_no'),)


class ImpInfo(models.Model):
    stdid = models.ForeignKey('Student', models.DO_NOTHING, db_column='STDID')  # Field name made lowercase.
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
    stdid = models.OneToOneField('Student', models.DO_NOTHING, db_column='STDID', primary_key=True)  # Field name made lowercase.
    semester = models.IntegerField(db_column='SEMESTER', blank=True, null=True)  # Field name made lowercase.
    subcode = models.ForeignKey(Department, models.DO_NOTHING, db_column='SUBCODE')  # Field name made lowercase.
    ia1_scores = models.IntegerField(db_column='IA1_SCORES', blank=True, null=True)  # Field name made lowercase.
    ia2_scores = models.IntegerField(db_column='IA2_SCORES', blank=True, null=True)  # Field name made lowercase.
    ia3_scores = models.IntegerField(db_column='IA3_SCORES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'marks'
        unique_together = (('stdid', 'subcode'),)


class Parent(models.Model):
    stdid = models.OneToOneField('Student', models.DO_NOTHING, db_column='STDID', primary_key=True)  # Field name made lowercase.
    pname = models.CharField(db_column='PNAME', max_length=100)  # Field name made lowercase.
    parent_or_gaurdian = models.CharField(db_column='PARENT_OR_GAURDIAN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    phone_no = models.IntegerField(db_column='PHONE_NO', blank=True, null=True)  # Field name made lowercase.
    alt_ph_no = models.IntegerField(db_column='ALT_PH_NO', blank=True, null=True)  # Field name made lowercase.
    father_occupation = models.CharField(db_column='FATHER_OCCUPATION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mother_occupation = models.CharField(db_column='MOTHER_OCCUPATION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email_id = models.CharField(db_column='EMAIL_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parent'
        unique_together = (('stdid', 'pname'),)


class Student(models.Model):
    sid = models.CharField(db_column='SID', primary_key=True, max_length=10)  # Field name made lowercase.
    student_fname = models.CharField(db_column='STUDENT_FNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    student_lname = models.CharField(db_column='STUDENT_LNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=7, blank=True, null=True)  # Field name made lowercase.
    email_id = models.CharField(db_column='EMAIL_ID', max_length=64, blank=True, null=True)  # Field name made lowercase.
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


class Teacher(models.Model):
    tid = models.CharField(db_column='TID', primary_key=True, max_length=10)  # Field name made lowercase.
    tname = models.CharField(db_column='TNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcode = models.ForeignKey(Department, models.DO_NOTHING, db_column='SUBCODE')  # Field name made lowercase.
    subname = models.CharField(db_column='SUBNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teacher'
        unique_together = (('tid', 'subcode'),)

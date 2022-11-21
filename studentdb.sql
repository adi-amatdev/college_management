create database if not exists SDB;

use SDB;

drop table if exists employees;

CREATE TABLE Student (
SID varchar(10) NOT NULL,
Student_name varchar(100) DEFAULT NULL,
Gender varchar(7) DEFAULT NULL,
Email_id varchar(64) DEFAULT NULL,
Current_Address varchar(300) DEFAULT NULL,
Permanent_Address varchar(300) DEFAULT NULL,
Cur_Sem int(5) DEFAULT NULL,
DOB date DEFAULT NULL,
HostelORDay_Scholar varchar(20) DEFAULT NULL,
DOC_return_status BOOLEAN DEFAULT 0,
PRIMARY KEY (SID)
);

CREATE TABLE ATTENDANCE(
STDID varchar(10) NOT NULL,
SUB_CODE varchar(7),
Classes_attended int(5) DEFAULT NULL,
total_classes int(5) DEFAULT NULL,
Percentage decimal(10,2) DEFAULT NULL,
FOREIGN KEY(STDID) REFERENCES Student(SID),
FOREIGN KEY(SUB_CODE) REFERENCES DEPARTMENT(SUBCODE)
);

CREATE TABLE Fees(
STDID varchar(10) NOT NULL,
College_fees int(10) DEFAULT NULL,
Hostel_fees int(10) DEFAULT NULL,
Library_fines int(5) DEFAULT NULL,
Other_fines int(5) DEFAULT NULL,
FOREIGN KEY(STDID) REFERENCES Student(SID)
);

CREATE TABLE Hostel(
STDID varchar(10) NOT NULL,
Girls_boys_Hostel varchar(5) DEFAULT NULL,
ROOM_NO varchar(5) DEFAULT NULL,
Block_name varchar(10) DEFAULT NULL,
FOREIGN KEY(STDID) REFERENCES Student(SID)
);

CREATE TABLE AADHAR(
    AADHAR_NO BIGINT NOT NULL,
    STID VARCHAR(10) NOT NULL,
    FOREIGN KEY(STID) REFERENCES Student(SID)
);

 CREATE TABLE PARENT(
    STDID varchar(10) NOT NULL,
    NAME VARCHAR(100),
    PARENT/GAURDIAN VARCHAR(15),
    PHONE_NO INT(10),
    ALT_PH_NO INT(10),
    OCCUPATION VARCHAR(50),
    EMAIL_ID VARCHAR(100),
    FOREIGN KEY(STDID) REFERENCES Student(SID)
 );
 
CREATE TABLE MARKS(
    STDID varchar(10) NOT NULL,
    SEMESTER INT NOT NULL,
    SUB_CODE VARCHAR(7),
    SEMESTER_SUB_SCORES BIGINT,
    NO_OF_BACKLOGS INT,
    BACK_LOG_SUB_CODE VARCHAR(10),
    FOREIGN KEY(STDID) REFERENCES Student(SID),
    FOREIGN KEY(SUB_CODE) REFERENCES DEPARTMENT(SUBCODE)
);
CREATE TABLE DEPARTMENT(
    STDID varchar(10) NOT NULL,
    DEPT_NAME VARCHAR(20),
    SUBCODE VARCHAR(10),
    SUBJECTNAME TEXT(30),
    DURATION INT,
    PRIMARY KEY (SUBCODE),
    FOREIGN KEY(STDID) REFERENCES Student(SID)
);
CREATE TABLE TEACHER(
    TID VARCHAR(10),
    TNAME VARCHAR(50),
    SUB_CODE VARCHAR(10),
    SUBNAME VARCHAR(20),
    PERSONAL_INFO VARCHAR(100),
    FOREIGN KEY(SUB_CODE) REFERENCES DEPARTMENT(SUBCODE)
);
CREATE TABLE IMP_INFO(
    STDID varchar(10) NOT NULL,
    10TH_PERCENTAGE BIGINT,
    12TH_PERCENTAGE BIGINT,
    NAME_OF_SCHOOL_10TH VARCHAR(20),
    NAME_OF_COLLEGE_12TH VARCHAR(20),
    BOARD_OF_EDUCATION_10TH VARCHAR(10),
    BOARD_OF_EDUCATION_12TH VARCHAR(10),
    YEAR_OF_PASSING_10TH INT,
    YEAR_OF_PASSING_12TH INT,
    EDUCATION_GAP INT,
    ADMISSION_QUOTA_NAME VARCHAR(10),
    RANK_FROM_ENTRANCE BIGINT,
    BANK_NAME VARCHAR(20),
    BANK_ACCOUNT_NO BIGINT,
    PAN_NO BIGINT,
    VOTER_ID_NO BIGINT,
    PASSPORT_NO BIGINT
    LINKDEN_ID VARCHAR(20),
    GITHUB_ID VARCHAR(20),
    AWARDS  VARCHAR(20),
    CERTIFICATES VARCHAR(20),
    FOREIGN KEY(STDID) REFERENCES Student(SID)
);
                  

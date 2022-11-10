create database if not exists SDB;

use SDB;

drop table if exists employees;

CREATE TABLE Student (
SID varchar(10) NOT NULL,
Student_name varchar(100) DEFAULT NULL,
Gender varchar(7) DEFAULT NULL,
Email_id varchar(64) DEFAULT NULL,
Address varchar(300) DEFAULT NULL,
Cur_Sem int(5) DEFAULT NULL,
DOB date DEFAULT NULL,
HostelORDay_Scholar varchar(20) DEFAULT NULL,
DOC_return_status varchar(20) DEFAULT NULL,
PRIMARY KEY (SID)
);


CREATE TABLE Attandance(
STDID varchar(10) NOT NULL,
Classes_attended int(5) DEFAULT NULL,
total_classes int(5) DEFAULT NULL,
Percentage decimal(10,2) DEFAULT NULL,
FOREIGN KEY(STDID) REFERENCES Student(SID)
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



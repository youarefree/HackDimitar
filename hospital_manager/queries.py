import sqlite3
import getpass
import datetime
from random import choice
from settings import DB_NAME
from hashing import *
import os


db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()

LIST_ALL_PATIENTS = '''SELECT * FROM
'''
REGISTER_IN_SYSTEM = '''INSERT INTO USER(USERNAME, PASSWORD, AGE)
VALUES(?, ?, ?)
'''

SELECT_ACADEMIC_TITLE = ''' SELECT ACADEMIC_TITLE
FROM DOCTOR JOIN USER
ON DOCTOR.ID = USER.ID
WHERE USER.ID = {}
'''

SELECT_USERS = '''SELECT * FROM USER
'''

INTO_THE_SYSTEM = '''UPDATE USER
SET IS_ACTIVE = 1
WHERE ID = {}
'''

OUT_OF_THE_SYSTEM = '''UPDATE USER
SET IS_ACTIVE = 0
WHERE ID = {}
'''

DROP_TABLE_ONLINE_USERS = '''DROP TABLE ONLINE_USERS'''

CREATE_TABLE_ONLINE_USERS = '''CREATE TABLE ONLINE_USERS(
ID INTEGER PRIMARY KEY,
USERNAME TEXT NOT NULL,

FOREIGN KEY (ID) references user(id)
)
'''

GET_PATIENTS_OF_DOCTOR = '''SELECT username
FROM user JOIN patient ON user.id = patient.id
JOIN doctor ON patient.doctor_id = doctor.id
WHERE doctor.id = {}
'''

LIST_ROOM_AND_DURATION_OF_PATIENT = '''SELECT hospital_stay.room, hospital_stay.startdate, hospital_stay.enddate
from hospital_stay join patient
on hospital_stay.patient_id = patient.id
join doctor on patient.doctor_id = doctor.id
where doctor.id = {}
'''

LIST_FREE_HOURS_OF_DOCTOR = '''SELECT DISTINCT *
FROM FREE_HOURS JOIN DOCTOR
ON free_hours.doctor_id = doctor.id
JOIN PATIENT ON patient.DOCTOR_ID = DOCTOR.ID
WHERE DOCTOR.ID = {}
'''

SELECT_DOCTOR_ID = '''SELECT DOCTOR_ID FROM PATIENT WHERE ID = {}
'''



# FILL_FREE_HOURS = '''INSERT INTO free_hours(FROM_TO, doctor_id)
# VALUES(?, ?)
# '''

# DROP_USER_TABLE = '''
#     DROP TABLE IF EXISTS USER
#  '''

# DROP_DOCTOR_TABLE = '''DROP TABLE IF EXISTS DOCTOR
# '''

# DROP_PATIENT_TABLE = '''DROP TABLE IF EXISTS PATIENT
# '''
# DROP_HOSPITAL_STAY_TABLE = '''DROP TABLE IF EXISTS HOSPITAL_STAY
# '''
# DROP_VISITATION_TABLE = '''DROP TABLE IF EXISTS VISITATION_TABLE
# '''

# CREATE_USER_TABLE = '''CREATE TABLE USER(
# ID INTEGER PRIMARY KEY AUTOINCREMENT,
# USERNAME TEXT NOT NULL,
# PASSWORD TEXT NOT NULL,
# AGE INT NOT NULL
# )
# '''

# CREATE_DOCTOR_TABLE = '''CREATE TABLE DOCTOR_TABLE
# '''

# CREATE_PATIENT_TABLE = '''CREATE TABLE
# '''

# CREATE_VISITATION_TABLE = '''
# '''

# CREATE_HOSPITAL_STAY_TABLE = '''
# '''


# def create_database():
#     c.execute(CREATE_USER_TABLE)
#     c.execute(CREATE_DOCTOR_TABLE)
#     c.execute(CREATE_PATIENT_TABLE)
#     c.execute(CREATE_HOSPITAL_STAY_TABLE)
#     c.execute(CREATE_VISITATION_TABLE)
#     db.commit()


# def drop_database_tables():
#     c.execute(DROP_USER_TABLE)
#     c.execute(DROP_DOCTOR_TABLE)
#     c.execute(DROP_PATIENT_TABLE)
#     c.execute(DROP_HOSPITAL_STAY_TABLE)
#     c.execute(DROP_VISITATION_TABLE)
#     db.commit()


# def insert_users():
# users = [('Dr. Albena Bachvarova', encode_pass('123456'), '47'),
#           ('Kristina Valchanova', encode_pass('123123'), '20'),
#           ('Dr. Pavlina Zdravkova', encode_pass('123456'), '47'),
#           ('Pandio Pandev', encode_pass('panda'), '4'),
#           ('Slayana Monkova', encode_pass('159357'), '21'),
#           ('Kiril Ivanov', encode_pass('kireto'), '21'),
#           ('Dr. Georgi Georgiev', encode_pass('159357'), '40'),
#           ('Dimitar Boyanov Yordanov', encode_pass('123456'), '47')
#           ]
#     c.executemany(INSERT_INTO_USER, users)
#     db.commit()


# def promote_to_doctors():
#     c.execute(SELECT_USERS)
#     users = c.fetchall()
#     doctors = []

#     for user in users:
#         if 'Dr.' in user['username']:
#             academic_title = choice(ACADEMIC_TITLES)
#             doctors.append((user['id'], academic_title))

#     c.executemany(PROMOTE_TO_DOCTOR, doctors)
#     db.commit()


# def promote_to_patients():
#     c.execute(SELECT_USERS)
#     users = c.fetchall()
#     patients = []
#     doctors = c.execute(SELECT_DOCTORS)
#     doc_ids = [doc['id'] for doc in doctors]

#     for user in users:
#         if 'Dr.' not in user['username']:
#             doctor = choice(doc_ids)
#             patients.append((user['id'], doctor))

#     c.executemany(PROMOTE_TO_PATIENT, patients)
#     db.commit()


# def add_hospital_stays():
#     c.execute(SELECT_PATIENTS)
#     patients = c.fetchall()

#     for patient in patients:
#         room = choice(ROOM_NUMBERS)
#         injury = choice(INJURIES)
#         startdate = str(datetime.datetime.now()).split()[0]
#         enddate = str(datetime.datetime.now()).split()[0]

#         c.execute(INSERT_INTO_HOSPITAL_STAY, (startdate,
#                                               enddate,
#                                               room,
#                                               injury,
#                                               patient['id']))
#     db.commit()


# def patient_visitations():
#     pass


# def create_and_fill_data():
#     drop_database_tables()
#     create_database()
#     insert_users()
#     promote_to_doctors()
#     promote_to_patients()
#     add_doctors_visitations()
#     add_hospital_stays()
#     patient_visitations()

# free_hours = [("Monday-Friday: 12:30 - 14:30", 1), ("Wednesday-Friday: 12:30 - 14:30", 3), ("Every day: 11:30 - 13:30", 7)]

def main():
    c.executemany(FILL_FREE_HOURS, free_hours)
    db.commit()


if __name__ == '__main__':
    main()

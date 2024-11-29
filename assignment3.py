import mysql.connector
from mysql.connector import Error
import datetime

def connectToDatabase():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="medical_service",
            user="root",
            password="", 
        )
        if connection.is_connected():
            print("Connected to the database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def insertPatients(connection):
    cursor = connection.cursor()
    patients = [
        ('Nguyen A', '2010-01-01', 'Male', 'Ha noi', '0123456789', 'nguyena@gmail.com'),
        ('Nguyen B', '1990-05-12', 'Female', 'Ha noi', '0123456790', 'nguyenb@gmail.com'),
        ('Nguyen C', '1985-08-20', 'Male', 'HCM', '0123456791', 'nguyenc@gmail.com')
    ]
    query = "INSERT INTO patients (full_name, date_of_birth, gender, address, phone_number, email) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.executemany(query, patients)
    connection.commit()
    print("Inserted 3 patients.")


def insertDoctors(connection):
    cursor = connection.cursor()
    doctors = [
        ('Nguyen Si', 'General Medicine', '0123456782', 'nguyensi@gmail.com', 5),
        ('Tran Binh', 'Cardiology', '0123456783', 'tranbinh@gmail.com', 8),
        ('Pham Mai', 'Neurology', '0123456784', 'phammai@gmail.com', 6),
        ('Le Hoang', 'Pediatrics', '0123456785', 'lehoang@gmail.com', 4),
        ('Nguyen Thao', 'Dermatology', '0123456786', 'nguyenthao@gmail.com', 10)
    ]
    query = "INSERT INTO doctors (full_name, specialization, phone_number, email, years_of_experience) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(query, doctors)
    connection.commit()
    print("Inserted 5 doctors.")


def insertAppointments(connection):
    cursor = connection.cursor()
    appointments = [
        (1, 1, '2024-11-29 10:00:00', 'Checkup'),
        (2, 2, '2024-11-29 11:00:00', 'Heart checkup'),
        (3, 3, '2024-11-29 14:00:00', 'Neurological exam')
    ]
    query = "INSERT INTO appointments (patient_id, doctor_id, appointment_date, reason) VALUES (%s, %s, %s, %s)"
    cursor.executemany(query, appointments)
    connection.commit()
    print("Inserted 3 appointments.")

def main():
    connection = connectToDatabase()
    if connection:
        insertPatients(connection)
        insertDoctors(connection)
        insertAppointments(connection)
        connection.close()

if __name__ == "__main__":
    main()

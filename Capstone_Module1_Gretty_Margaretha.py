# List Data Pasien dan Janji Temu
patient_records = [
    {
        'Medical Record Number': 'MGH_0001',
        'Name': 'Emily Thompson',
        'Age': 82,
        'Gender' : 'female',
        'Diagnosis' : 'Hypertension (High Blood Pressure), Type 2 Diabetes Mellitus'
    },
    {
        'Medical Record Number': 'MGH_0002',
        'Name': 'Jason Rodriguez',
        'Age': 55,
        'Gender' : 'male',
        'Diagnosis' : 'Asthma',
        'Appointments': [
            {
                'Doctor': 'Dr. Wilson',
                'Date': '25-02-2022',
                'Time': '11:30 AM',
                'Notes': 'Initial consultation'
            }
        ]
    },
    {
        'Medical Record Number': 'MGH_0003',
        'Name': 'Patel Ang',
        'Age': 39,
        'Gender' : 'male',
        'Diagnosis' : 'Chronic Obstructive Pulmonary Disease (COPD), Rheumatoid Arthritis, Major Depressive Disorder',
        'Appointments': [
            {
                'Doctor': 'Dr. Smith',
                'Date': '20-02-2022',
                'Time': '10:00 AM',
                'Notes': 'Regular checkup'
            },
            {
                'Doctor': 'Dr. Johnson',
                'Date': '15-03-2022',
                'Time': '02:30 PM',
                'Notes': 'Follow-up appointment'
            }
        ]
    },
    {
        'Medical Record Number': 'MGH_0004',
        'Name': 'Elijah Williams',
        'Age': 72,
        'Gender' : 'female',
        'Diagnosis' : 'Osteoarthritis, Hyperlipidemia (High Cholesterol)'
    },
    {
        'Medical Record Number': 'MGH_0005',
        'Name': 'Sophia Ra-Chang',
        'Age': 28,
        'Gender' : 'female',
        'Diagnosis' : 'Thyroid Dysfunction (e.g., Hypothyroidism)'
    }
]

# Fungsi untuk melihat data pasien
from tabulate import tabulate

def view_all_patients(): # fiture
    headers = ['MR Number', 'Name', 'Age', 'Gender', 'Diagnosis']
    data = []

    for patient_data in patient_records:
        row = [patient_data['Medical Record Number'],
               patient_data['Name'],
               patient_data['Age'],
               patient_data['Gender'],
               patient_data['Diagnosis']]
        data.append(row) #list row akan ditambahkan ke dalam list data.

    print('\nPatient Records\n')
    print(tabulate(data, headers=headers, tablefmt='github'))

    
# Fungsi untuk menambah data pasien
def add_patient():
    if patient_records:
        # membagi string menjadi beberapa bagian berdasarkan karakter pemisah underscore (_)
        last_medical_record_number = int(patient_records[-1]['Medical Record Number'].split('_')[-1])
        new_medical_record_number = f"MGH_{(last_medical_record_number + 1):04d}"
    else:
        new_medical_record_number = "MGH_0001" # memberikan nomor rekam medis default jika tidak ada nomor rekam medis yang ada

    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter patient gender: ")
    diagnosis = input("Enter patient diagnosis: ")

    patient_records.append({
        'Medical Record Number': new_medical_record_number,
        'Name': name,
        'Age': age,
        'Gender': gender,
        'Diagnosis': diagnosis
    })

    print("\nPatient data added successfully.")

# Fungsi untuk mencari data pasien berdasarkan Nomor Rekam Medis
def search_patient_by_medical_record_number():
    medical_record_number = input("\nEnter medical record number to search (MGH_xxxx): ")
    for patient_data in patient_records:
        if patient_data['Medical Record Number'] == medical_record_number:
            print("\nPatient Found:")
            max_key_length = max(len(key) for key in patient_data.keys())
            for key, value in patient_data.items():
                if key == 'Appointments':
                    break  # Stop printing when reaching 'Appointments'
                spacing = ' ' * (max_key_length - len(key))
                print(f"{key}{spacing}\t:{value}")
            return
    else:
        print("Patient not found.")

# Fungsi untuk memperbarui data pasien
def update_patient_data():
    medical_record_number = input("\nEnter medical record number to update (MGH_xxxx): ")
    for patient_data in patient_records:
        if patient_data['Medical Record Number'] == medical_record_number:
            print(f"\nCurrent Data for Medical Record Number {medical_record_number}:")
            max_key_length = max(len(key) for key in patient_data.keys())
            for key, value in patient_data.items():
                spacing = ' ' * (max_key_length - len(key))
                print(f"{key}{spacing}\t:{value}")

            # Menanyakan data apa yang ingin diperbarui
            update_choice = input("\nChoose data to update:\n1. Name\n2. Age\n3. Gender\n4. Diagnosis\nEnter your choice (1-4): ")

            if update_choice == '1':
                new_name = input("\nEnter new name: ")
                patient_data['Name'] = new_name
            elif update_choice == '2':
                new_age = input("\nEnter new age: ")
                patient_data['Age'] = new_age
            elif update_choice == '3':
                new_gender = input("\nEnter new gender: ")
                patient_data['Gender'] = new_gender
            elif update_choice == '4':
                # Menanyakan apakah pengguna ingin menambahkan atau mengganti keseluruhan diagnosis
                operation_choice = input("\nDo you want to (1) append or (2) replace the diagnosis? Enter 1 or 2: ")
                if operation_choice == '1':
                    # Pengguna ingin menambahkan diagnosis
                    new_diagnosis = input("\nEnter new diagnosis to append: ")
                    # Konversi string diagnosis awalnya menjadi list
                    if not isinstance(patient_data['Diagnosis'], list):
                        patient_data['Diagnosis'] = [patient_data['Diagnosis']]
                    # Menambahkan diagnosis baru ke list
                    patient_data['Diagnosis'].append(new_diagnosis)
                    print("\nDiagnosis appended successfully.")
                elif operation_choice == '2':
                    # Pengguna ingin mengganti keseluruhan diagnosis
                    new_diagnosis = input("\nEnter new diagnosis to replace the current diagnosis: ")
                    patient_data['Diagnosis'] = [new_diagnosis]
                    print("\nDiagnosis replaced successfully.")
                else:
                    print("\nInvalid choice. Please enter either 1 or 2.")
            print("\nPatient data updated successfully.")
            return
    else:
        print("Patient not found.")

    
# Fungsi untuk menambah janji temu
def add_appointment():
    medical_record_number = input("\nEnter medical record number to search: ")
    for patient_data in patient_records:
        if patient_data['Medical Record Number'] == medical_record_number:
            doctor_name = input("Enter doctor's name: ")
            appointment_date = input("Enter appointment date (DD-MM-YYYY): ")
            appointment_time = input("Enter appointment time (e.g 10:00 AM): ")
            additional_notes = input("Enter additional notes: ")

            appointment = {
                'Doctor': doctor_name,
                'Date': appointment_date,
                'Time': appointment_time,
                'Notes': additional_notes
            }
            
            if 'Appointments' not in patient_data:
                patient_data['Appointments'] = []

            
            patient_data['Appointments'].append(appointment)

            print("Appointment added successfully.")
            break
    else:
        print("Patient not found. Please add the patient first.")
        
# Fungsi untuk melihat semua janji temu
def view_all_appointments():
    headers = ['MR Number', 'Doctor Name', 'Date', 'Time', 'Note']
    data = []

    for patient_data in patient_records:
        appointments = patient_data.get('Appointments', [])
        
        for appointment in appointments:
            row = [
                patient_data.get('Medical Record Number', 'N/A'),
                appointment.get('Doctor', 'N/A'),
                appointment.get('Date', 'N/A'),
                appointment.get('Time', 'N/A'),
                appointment.get('Notes', 'N/A')
            ]
            data.append(row)

    print('\nAppointments\n')
    print(tabulate(data, headers=headers, tablefmt='github'))



#Loop utama untuk menu interaktif
while True:
    main_choice = input('''
    \tWelcome to Massachusetts General Hospital
    Where compassionate care meets medical excellence
        
        Main Menu:
        1. Patient Management
        2. Appointment Management
        3. Exit
    \nEnter your choice (1-3): ''')

    if main_choice == '1':
        while True:  # Loop untuk submenu Patient Management
            patient_choice = input('''\n
            Patient Management:
            1. View All Patients
            2. Add Patient
            3. Search Patient by Medical Record Number
            4. Update Patient Data
            5. Back to Main Menu

            \nEnter your choice (1-5): ''')

            if patient_choice == '1':
                view_all_patients()
            elif patient_choice == '2':
                add_patient()
            elif patient_choice == '3':
                search_patient_by_medical_record_number()
            elif patient_choice == '4':
                update_patient_data()
            elif patient_choice == '5':
                break  # Keluar dari loop inner
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
    
    elif main_choice == '2':
        while True:  # Loop untuk submenu Appointment Management
            appointment_choice = input('''\n
            Appointment Management:
            1. Add Appointment
            2. View All Appointments
            3. Back to Main Menu

            \nEnter your choice (1-3): ''')

            if appointment_choice == '1':
                add_appointment()
            elif appointment_choice == '2':
                view_all_appointments()
            elif appointment_choice == '3':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
    
    elif main_choice == '3':
        print("\nThank you for choosing Massachusetts General Hospital for your healthcare needs\nYour well-being is our priority\n\n")
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")


        
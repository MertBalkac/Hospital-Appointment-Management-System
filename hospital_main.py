
import hospital_abstractions as a

def main():
    """Run the main command-line interface for the hospital appointment system."""
    # Create 3 hospitals
    list_of_hospitals = ['City Hospital', 'Sunrise Clinic', 'General Hospital']
    list_of_appointments = [100, 50, 150]
    for hospital, appointments in zip(list_of_hospitals, list_of_appointments):
        a.create_hospital(hospital, appointments)

    # Display all hospitals
    print('Displaying all hospitals...')
    for hospital in list_of_hospitals:
        a.display_hospital(hospital)
    print()

    # Create 9 patients
    list_of_patients = [
        'Mert Balkac', 'Can Balkac', 'Firdes Balkac', 'Harun Durmus', 
        'Ozge Arica', 'Sarper Eroglan', 'Atakan Karaca', 'Efe Kutuk', 
        'Ogulcan Yildirim'
    ]
    for patient in list_of_patients:
        a.create_patient(patient)

    # Display all patients
    print('Displaying all patients...')
    for patient in list_of_patients:
        a.display_patient(patient)
    print()

    # Create 9 appointments
    a.schedule_appointment('Mert Balkac', 'City Hospital')
    a.schedule_appointment('Can Balkac', 'City Hospital')
    a.schedule_appointment('Firdes Balkac', 'City Hospital')
    a.schedule_appointment('Harun Durmus', 'Sunrise Clinic')
    a.schedule_appointment('Ozge Arica', 'Sunrise Clinic')
    a.schedule_appointment('Sarper Eroglan', 'Sunrise Clinic')
    a.schedule_appointment('Atakan Karaca', 'General Hospital')
    a.schedule_appointment('Efe Kutuk', 'General Hospital')
    a.schedule_appointment('Ogulcan Yildirim', 'General Hospital')

    # Display all hospitals
    print('Displaying all hospitals with new appointments...')
    for hospital in list_of_hospitals:
        a.display_hospital(hospital)
    print()

    # Modify hospitals
    a.modify_hospital('City Hospital', 200)
    a.modify_hospital('Sunrise Clinic', 100)
    a.modify_hospital('General Hospital', 300)

    # Display all hospitals
    print('Displaying all hospitals with modified available appointments...')
    for hospital in list_of_hospitals:
        a.display_hospital(hospital)
    print()

    # Modify 6 patients
    old_names = [
        'Mert Balkac', 'Can Balkac', 'Firdes Balkac', 'Harun Durmus', 
        'Ozge Arica', 'Sarper Eroglan'
    ]
    new_names = [
        'Mert Updated', 'Can Updated', 'Firdes Updated', 'Harun Updated', 
        'Ozge Updated', 'Sarper Updated'
    ]
    for old, new in zip(old_names, new_names):
        a.modify_patient(old, new)

    # Display all patients
    print('Displaying all patients with modified names...')
    list_of_patients = [
        'Mert Updated', 'Can Updated', 'Firdes Updated', 'Harun Updated', 
        'Ozge Updated', 'Sarper Updated', 'Atakan Karaca', 'Efe Kutuk', 
        'Ogulcan Yildirim'
    ]
    for patient in list_of_patients:
        a.display_patient(patient)
    print()

    # Display all hospitals
    print('Displaying all hospitals with modified appointments...')
    for hospital in list_of_hospitals:
        a.display_hospital(hospital)
    print()

    # Cancel 6 appointments
    a.cancel_appointment('Mert Updated', 'City Hospital')
    a.cancel_appointment('Can Updated', 'City Hospital')
    a.cancel_appointment('Firdes Updated', 'City Hospital')
    a.cancel_appointment('Harun Updated', 'Sunrise Clinic')
    a.cancel_appointment('Ozge Updated', 'Sunrise Clinic')
    a.cancel_appointment('Sarper Updated', 'Sunrise Clinic')

    # Display all hospitals
    print('Displaying all hospitals with cancelled appointments...')
    for hospital in list_of_hospitals:
        a.display_hospital(hospital)

if __name__ == "__main__":
    main()

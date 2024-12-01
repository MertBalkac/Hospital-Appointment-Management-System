
import json
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Hospital:
    def __init__(self, name, appointments):
        self.name = name
        self.appointments = appointments
        self.reservations = []

    def schedule_appointment(self, patient):
        if self.appointments > 0:
            self.appointments -= 1
            self.reservations.append(patient.name)
            logging.info(f"Appointment scheduled: {patient.name} at {self.name}")
            return True
        logging.critical(f"No available appointments at {self.name} for {patient.name}")
        return False

    def cancel_appointment(self, patient):
        if patient.name in self.reservations:
            self.appointments += 1
            self.reservations.remove(patient.name)
            logging.info(f"Appointment cancelled: {patient.name} at {self.name}")
            return True
        logging.critical(f"No appointment found for {patient.name} at {self.name} to cancel")
        return False

    def update_appointment(self, old_name, new_name):
        if old_name in self.reservations:
            self.reservations.remove(old_name)
            self.reservations.append(new_name)
            logging.info(f"Appointment updated: {old_name} replaced with {new_name} at {self.name}")
            return True
        logging.critical(f"Failed to update appointment: {old_name} not found at {self.name}. Current reservations: {self.reservations}")
        return False

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        hospital = cls(data['name'], data['appointments'])
        hospital.reservations = data['reservations']
        return hospital


class Patient:
    def __init__(self, name):
        self.name = name

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(data['name'])


def save_to_file(obj, filename):
    try:
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(obj.to_json())
        logging.info(f"File saved: {filename}")
    except Exception as e:
        logging.critical(f"Failed to save file {filename}: {e}")


def load_from_file(cls, filename):
    try:
        if os.path.exists(filename):
            with open(filename, 'r', encoding="utf-8") as file:
                logging.info(f"File loaded: {filename}")
                return cls.from_json(file.read())
        else:
            logging.critical(f"File not found: {filename}")
            return None
    except json.JSONDecodeError as e:
        logging.critical(f"Invalid JSON data in file {filename}: {e}")
        return None
    except FileNotFoundError:
        logging.critical(f"File not found: {filename}")
        return None


def create_hospital(name, appointments):
    hospital = Hospital(name, appointments)
    save_to_file(hospital, f'{name}.hospital')


def delete_hospital(name):
    if os.path.exists(f'{name}.hospital'):
        os.remove(f'{name}.hospital')
        logging.info(f"Hospital deleted: {name}")
    else:
        logging.critical(f"Hospital not found: {name}")


def display_hospital(name):
    hospital = load_from_file(Hospital, f'{name}.hospital')
    if hospital:
        print(f'Hospital Name: {hospital.name}')
        print(f'Available Appointments: {hospital.appointments}')
        print('Scheduled Appointments:')
        for patient in hospital.reservations:
            print(f' - {patient}')
    else:
        logging.critical(f"Hospital not found: {name}")


def modify_hospital(name, new_appointments):
    hospital = load_from_file(Hospital, f'{name}.hospital')
    if hospital and new_appointments is not None:
        appointment_difference = new_appointments - (hospital.appointments + len(hospital.reservations))
        hospital.appointments += appointment_difference
        hospital.appointments = max(hospital.appointments, 0)
        save_to_file(hospital, f'{name}.hospital')
        logging.info(f"Hospital modified: {name} now has {hospital.appointments} available appointments")
    else:
        logging.critical(f"Failed to modify hospital: {name}")


def create_patient(name):
    patient = Patient(name)
    save_to_file(patient, f'{name}.patient')


def delete_patient(name):
    if os.path.exists(f'{name}.patient'):
        os.remove(f'{name}.patient')
        logging.info(f"Patient deleted: {name}")
    else:
        logging.critical(f"Patient not found: {name}")


def display_patient(name):
    patient = load_from_file(Patient, f'{name}.patient')
    if patient:
        print(f'Patient Name: {patient.name}')
    else:
        logging.critical(f"Patient not found: {name}")


def modify_patient(old_name, new_name):
    patient = load_from_file(Patient, f'{old_name}.patient')
    if patient:
        patient.name = new_name
        save_to_file(patient, f'{new_name}.patient')
        if old_name != new_name:
            os.remove(f'{old_name}.patient')
            for hospital_file in os.listdir():
                if hospital_file.endswith('.hospital'):
                    hospital = load_from_file(Hospital, hospital_file)
                    if hospital.update_appointment(old_name, new_name):
                        save_to_file(hospital, hospital_file)
        logging.info(f"Patient modified: {old_name} renamed to {new_name}")
    else:
        logging.critical(f"Failed to modify patient: {old_name}")


def schedule_appointment(patient_name, hospital_name):
    patient = load_from_file(Patient, f'{patient_name}.patient')
    hospital = load_from_file(Hospital, f'{hospital_name}.hospital')
    if patient and hospital:
        if hospital.schedule_appointment(patient):
            save_to_file(hospital, f'{hospital_name}.hospital')  # Save changes after scheduling
    else:
        logging.critical(f"Failed to schedule appointment: Patient {patient_name} or Hospital {hospital_name} not found")


def cancel_appointment(patient_name, hospital_name):
    patient = load_from_file(Patient, f'{patient_name}.patient')
    hospital = load_from_file(Hospital, f'{hospital_name}.hospital')
    if patient and hospital:
        if hospital.cancel_appointment(patient):
            save_to_file(hospital, f'{hospital_name}.hospital')  # Save changes after cancellation
    else:
        logging.critical(f"Failed to cancel appointment: Patient {patient_name} or Hospital {hospital_name} not found")

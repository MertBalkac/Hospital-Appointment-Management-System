
import unittest
from unittest import mock
import os
import hospital_abstractions as a


class TestHospital(unittest.TestCase):
    def setUp(self):
        self.hospital = a.Hospital('Test Hospital', 10)
        self.patient = a.Patient('Test Patient')

    def test_schedule_appointment(self):
        self.assertTrue(self.hospital.schedule_appointment(self.patient))
        self.assertEqual(self.hospital.appointments, 9)
        self.assertIn(self.patient.name, self.hospital.reservations)

    def test_cancel_appointment(self):
        self.hospital.schedule_appointment(self.patient)
        self.assertTrue(self.hospital.cancel_appointment(self.patient))
        self.assertEqual(self.hospital.appointments, 10)
        self.assertNotIn(self.patient.name, self.hospital.reservations)

    def test_update_appointment(self):
        # Ensure appointment is scheduled before updating
        self.hospital.schedule_appointment(self.patient)
        print("Before update: Current reservations:", self.hospital.reservations)

        new_patient = a.Patient('New Patient')
        self.assertTrue(self.hospital.update_appointment(
            self.patient.name, new_patient.name)
        )
        self.assertIn(new_patient.name, self.hospital.reservations)
        self.assertNotIn(self.patient.name, self.hospital.reservations)

        print("After update: Current reservations:", self.hospital.reservations)

    def test_to_json(self):
        self.assertEqual(
            self.hospital.to_json(),
            '{"name": "Test Hospital", "appointments": 10, "reservations": []}'
        )

    def test_from_json(self):
        json_str = '{"name": "Test Hospital", "appointments": 10, "reservations": []}'
        hospital = a.Hospital.from_json(json_str)
        self.assertEqual(hospital.name, 'Test Hospital')
        self.assertEqual(hospital.appointments, 10)
        self.assertEqual(hospital.reservations, [])


class TestPatient(unittest.TestCase):
    def setUp(self):
        self.patient = a.Patient('Test Patient')

    def test_to_json(self):
        self.assertEqual(self.patient.to_json(), '{"name": "Test Patient"}')

    def test_from_json(self):
        json_str = '{"name": "Test Patient"}'
        patient = a.Patient.from_json(json_str)
        self.assertEqual(patient.name, 'Test Patient')


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.hospital_name = 'Test Hospital'
        self.patient_name = 'Test Patient'
        self.hospital = a.Hospital(self.hospital_name, 10)
        self.patient = a.Patient(self.patient_name)
        a.save_to_file(self.hospital, f'{self.hospital_name}.hospital')
        a.save_to_file(
            self.patient, f'{self.patient_name}.patient'
        )

    def tearDown(self):
        if os.path.exists(f'{self.hospital_name}.hospital'):
            os.remove(f'{self.hospital_name}.hospital')
        if os.path.exists(f'{self.patient_name}.patient'):
            os.remove(f'{self.patient_name}.patient')

    def test_schedule_and_cancel_appointment(self):
        a.schedule_appointment(self.patient_name, self.hospital_name)
        hospital = a.load_from_file(
            a.Hospital, f'{self.hospital_name}.hospital'
        )
        print("After scheduling: Current reservations:", hospital.reservations)
        self.assertIn(self.patient_name, hospital.reservations)

        a.cancel_appointment(self.patient_name, self.hospital_name)
        hospital = a.load_from_file(
            a.Hospital, f'{self.hospital_name}.hospital'
        )
        print("After cancellation: Current reservations:", hospital.reservations)
        self.assertNotIn(self.patient_name, hospital.reservations)


class TestDisplayFunctions(unittest.TestCase):
    def setUp(self):
        self.hospital_name = 'Test Hospital'
        self.patient_name = 'Test Patient'
        self.hospital = a.Hospital(self.hospital_name, 10)
        self.patient = a.Patient(self.patient_name)
        a.save_to_file(self.hospital, f'{self.hospital_name}.hospital')
        a.save_to_file(
            self.patient, f'{self.patient_name}.patient'
        )

    def tearDown(self):
        if os.path.exists(f'{self.hospital_name}.hospital'):
            os.remove(f'{self.hospital_name}.hospital')
        if os.path.exists(f'{self.patient_name}.patient'):
            os.remove(f'{self.patient_name}.patient')

    @mock.patch('builtins.print')
    def test_display_hospital(self, mock_print):
        a.display_hospital(self.hospital_name)
        mock_print.assert_any_call('Hospital Name: Test Hospital')
        mock_print.assert_any_call('Available Appointments: 10')
        mock_print.assert_any_call('Scheduled Appointments:')

    @mock.patch('builtins.print')
    def test_display_patient(self, mock_print):
        a.display_patient(self.patient_name)
        mock_print.assert_any_call('Patient Name: Test Patient')


if __name__ == '__main__':
    unittest.main()

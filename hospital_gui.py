
import tkinter as tk
from tkinter import messagebox, ttk
import hospital_abstractions as a
import os

class HospitalManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Appointment Management System")
        self.root.geometry("800x600")

        # Main menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.menu.add_command(label="View Hospitals", command=self.view_hospitals)
        self.menu.add_command(label="View Patients", command=self.view_patients)
        self.menu.add_command(label="Add Hospital", command=self.add_hospital)
        self.menu.add_command(label="Add Patient", command=self.add_patient)
        self.menu.add_command(label="Make Appointment", command=self.make_appointment)
        self.menu.add_command(label="Cancel Appointment", command=self.cancel_appointment)
        self.menu.add_command(label="View Reservations", command=self.view_reservations)

        # Frame for dynamic content
        self.content_frame = tk.Frame(self.root)
        self.content_frame.pack(fill="both", expand=True)

        tk.Label(self.content_frame, text="Welcome to the Hospital Management System",
                 font=("Arial", 16)).pack(pady=20)

    def clear_frame(self):
        '''Clear the content frame.'''
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def view_hospitals(self):
        '''View all hospitals.'''
        self.clear_frame()
        tk.Label(self.content_frame, text="Existing Hospitals", font=("Arial", 14)).pack(pady=10)

        hospital_list = tk.Text(self.content_frame, height=20, width=50)
        hospital_list.pack(pady=10)

        for hospital_file in [f for f in os.listdir() if f.endswith(".hospital")]:
            hospital = a.load_from_file(a.Hospital, hospital_file)
            hospital_list.insert(
                tk.END, f"{hospital.name}: {hospital.appointments} available appointments\n"
            )

    def view_patients(self):
        '''View all patients.'''
        self.clear_frame()
        tk.Label(self.content_frame, text="Existing Patients", font=("Arial", 14)).pack(pady=10)

        patient_list = tk.Text(self.content_frame, height=20, width=50)
        patient_list.pack(pady=10)

        for patient_file in [f for f in os.listdir() if f.endswith(".patient")]:
            patient = a.load_from_file(a.Patient, patient_file)
            patient_list.insert(tk.END, f"{patient.name}\n")

    def add_hospital(self):
        '''Add a new hospital.'''
        self.clear_frame()
        tk.Label(self.content_frame, text="Add Hospital", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.content_frame, text="Hospital Name").pack(pady=5)
        hospital_name = tk.Entry(self.content_frame)
        hospital_name.pack(pady=5)

        tk.Label(self.content_frame, text="Available Appointments").pack(pady=5)
        appointments = tk.Entry(self.content_frame)
        appointments.pack(pady=5)

        def create_hospital():
            name = hospital_name.get()
            appt = int(appointments.get())
            a.create_hospital(name, appt)
            messagebox.showinfo("Success", f"Hospital '{name}' created with {appt} appointments.")
            hospital_name.delete(0, tk.END)
            appointments.delete(0, tk.END)

        tk.Button(self.content_frame, text="Create Hospital", command=create_hospital).pack(pady=10)

    def add_patient(self):
        '''Add a new patient.'''
        self.clear_frame()
        tk.Label(self.content_frame, text="Add Patient", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.content_frame, text="Patient Name").pack(pady=5)
        patient_name = tk.Entry(self.content_frame)
        patient_name.pack(pady=5)

        def create_patient():
            name = patient_name.get()
            a.create_patient(name)
            messagebox.showinfo("Success", f"Patient '{name}' created.")
            patient_name.delete(0, tk.END)

        tk.Button(self.content_frame, text="Create Patient", command=create_patient).pack(pady=10)

    def make_appointment(self):
        '''Make an appointment with dropdown menus for selection.'''
        self.clear_frame()
        tk.Label(self.content_frame, text="Make Appointment", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.content_frame, text="Patient").pack(pady=5)
        patient_names = [f.split('.')[0] for f in os.listdir() if f.endswith(".patient")]
        patient_dropdown = ttk.Combobox(self.content_frame, values=patient_names)
        patient_dropdown.pack(pady=5)

        tk.Label(self.content_frame, text="Hospital").pack(pady=5)
        hospital_names = [f.split('.')[0] for f in os.listdir() if f.endswith(".hospital")]
        hospital_dropdown = ttk.Combobox(self.content_frame, values=hospital_names)
        hospital_dropdown.pack(pady=5)

        def schedule_appointment():
            patient = patient_dropdown.get()
            hospital = hospital_dropdown.get()
            a.schedule_appointment(patient, hospital)
            messagebox.showinfo("Success", f"Appointment scheduled for {patient} at {hospital}.")
            patient_dropdown.set('')
            hospital_dropdown.set('')

        tk.Button(self.content_frame, text="Schedule Appointment", command=schedule_appointment).pack(pady=10)

    def cancel_appointment(self):
        '''Cancel an appointment with dropdown menus for selection.'''
        self.clear_frame()
        tk.Label(self.content_frame, text="Cancel Appointment", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.content_frame, text="Patient").pack(pady=5)
        patient_names = [f.split('.')[0] for f in os.listdir() if f.endswith(".patient")]
        patient_dropdown = ttk.Combobox(self.content_frame, values=patient_names)
        patient_dropdown.pack(pady=5)

        tk.Label(self.content_frame, text="Hospital").pack(pady=5)
        hospital_names = [f.split('.')[0] for f in os.listdir() if f.endswith(".hospital")]
        hospital_dropdown = ttk.Combobox(self.content_frame, values=hospital_names)
        hospital_dropdown.pack(pady=5)

        def cancel_appt():
            patient = patient_dropdown.get()
            hospital = hospital_dropdown.get()
            a.cancel_appointment(patient, hospital)
            messagebox.showinfo("Success", f"Appointment for {patient} at {hospital} has been canceled.")
            patient_dropdown.set('')
            hospital_dropdown.set('')

        tk.Button(self.content_frame, text="Cancel Appointment", command=cancel_appt).pack(pady=10)

    def view_reservations(self):
        '''View all existing reservations in hospitals.'''
        self.clear_frame()
        tk.Label(self.content_frame, text="All Reservations", font=("Arial", 14)).pack(pady=10)

        reservation_list = tk.Text(self.content_frame, height=20, width=50)
        reservation_list.pack(pady=10)

        for hospital_file in [f for f in os.listdir() if f.endswith(".hospital")]:
            hospital = a.load_from_file(a.Hospital, hospital_file)
            reservation_list.insert(
                tk.END, f"{hospital.name}: {', '.join(hospital.reservations) or 'No Reservations'}\n"
            )

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementApp(root)
    root.mainloop()

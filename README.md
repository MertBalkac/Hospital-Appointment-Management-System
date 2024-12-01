
# Hospital Appointment Management System

## Overview
The **Hospital Appointment Management System** allows users to manage hospitals, patients, and appointments seamlessly through a graphical user interface (GUI). This system provides functionalities such as scheduling, updating, canceling appointments, managing hospital and patient data, and viewing reservations.

Additionally, the project includes a robust unit testing framework to validate all functionalities. Users can run tests to ensure the system works as expected.

---

## Features
- **View Hospitals:**
  - List all hospitals with their available appointments.
- **View Patients:**
  - List all registered patients.
- **Add Hospital:**
  - Add a new hospital with a specified number of available appointments.
- **Add Patient:**
  - Add a new patient to the system.
- **Make Appointment:**
  - Schedule a patient to a hospital using dropdown menus for selection.
- **Cancel Appointment:**
  - Cancel an existing appointment using dropdown menus for selection.
- **View Reservations:**
  - Display all reservations across all hospitals.

---

## Testing and Validation

The project includes a test suite (`hospital_tests.py`) that validates all key functionalities. These tests ensure that:

- Hospitals can be created, modified, and deleted correctly.
- Patients can be created, modified, and deleted correctly.
- Appointments can be scheduled, updated, and canceled successfully.
- Data is saved and loaded correctly from `.hospital` and `.patient` files.

### Running Tests
To run the test suite, execute the following command in your terminal:
```bash
python -m unittest hospital_tests.py
```

### Expected Output
All tests should pass, and you should see output similar to this:
```
...........
----------------------------------------------------------------------
Ran 11 tests in 0.003s

OK
```

If any test fails, the output will indicate the cause, making debugging straightforward.

---

## Setup Instructions

### Prerequisites
- Python 3.7 or higher installed on your system.
- A code editor or IDE (e.g., VS Code, PyCharm).

### Installation
1. **Clone or Download the Repository:**
   ```bash
   git clone <repository-link>
   cd hospital-management-system
   ```

2. **Ensure Required Files Exist:**
   - `hospital_abstractions.py`: Core logic for hospital, patient, and appointment management.
   - `hospital_gui.py`: GUI application for the system.
   - `hospital_tests.py`: Unit test suite for functionality validation.

3. **Run the GUI Application:**
   To launch the graphical interface:
   ```bash
   python hospital_gui.py
   ```

---

## Usage Instructions

### 1. **View Hospitals**
- Navigate to "View Hospitals" from the menu to see a list of all hospitals and their available appointments.

### 2. **View Patients**
- Navigate to "View Patients" from the menu to see a list of all registered patients.

### 3. **Add Hospital**
- Navigate to "Add Hospital" from the menu.
- Enter the hospital name and the number of available appointments.
- Click "Create Hospital" to save.

### 4. **Add Patient**
- Navigate to "Add Patient" from the menu.
- Enter the patient's name and click "Create Patient" to save.

### 5. **Make Appointment**
- Navigate to "Make Appointment" from the menu.
- Select a patient and a hospital from the dropdown menus.
- Click "Schedule Appointment" to create the appointment.

### 6. **Cancel Appointment**
- Navigate to "Cancel Appointment" from the menu.
- Select a patient and a hospital from the dropdown menus.
- Click "Cancel Appointment" to remove the appointment.

### 7. **View Reservations**
- Navigate to "View Reservations" from the menu.
- See all reservations listed for each hospital.

---

## File Structure
```
hospital-management-system/
├── hospital_abstractions.py    # Core logic for hospitals, patients, and appointments.
├── hospital_gui.py             # Main GUI application for the system.
├── hospital_tests.py           # Unit tests for functionality validation.
├── README.md                   # Project documentation.
```

---

## Logging
The system uses Python's `logging` module for debugging and tracking operations:
- **INFO:** Successful operations (e.g., appointment scheduled, file saved).
- **CRITICAL:** Errors requiring attention (e.g., file not found, invalid data).

---

## Future Enhancements
- Implement authentication and user roles.
- Add a database for persistent and scalable data storage.
- Integrate an analytics dashboard to visualize appointment trends.

---


"""
Hospital Management System
This system manages Hospitals, Departments, Staff, and Patients using OOP principles.
"""

class Person:
    """
    Base class representing a general person.
    """
    def __init__(self, name: str, age: int):
        """
        Initialize a Person instance.
        :param name: Name of the person
        :param age: Age of the person
        """
        self.name = name
        self.age = age

    def view_info(self) -> str:
        """
        Returns a string representation of the person's basic info.
        """
        return f"Name: {self.name}, Age: {self.age}"


class Staff(Person):
    """
    Represents hospital employees, inheriting from Person.
    """
    def __init__(self, name: str, age: int, position: str):
        """
        Initialize a Staff instance.
        :param position: Job title or role
        """
        super().__init__(name, age)
        self.position = position

    def view_info(self) -> str:
        """
        Overrides Person.view_info to include staff position.
        """
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}"


class Patient(Person):
    """
    Represents hospital patients, inheriting from Person.
    """
    def __init__(self, name: str, age: int, medical_record: str):
        """
        Initialize a Patient instance.
        :param medical_record: Patient's medical history
        """
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_info(self) -> str:
        """
        Overrides Person.view_info.
        """
        return f"Name: {self.name}, Age: {self.age}"

    def view_record(self) -> str:
        """
        Returns the patient's medical record.
        """
        return f"Medical Record: {self.medical_record} Patient"


class Department:
    """
    Manages staff and patients within a specific hospital department.
    """
    def __init__(self, name: str):
        """
        Initialize a Department instance.
        :param name: Name of the department
        """
        self.name = name
        self.staff = []    # List to store Staff objects
        self.patients = [] # List to store Patient objects

    def add_patient(self, patient: Patient):
        """
        Adds a patient object to the department.
        """
        self.patients.append(patient)

    def add_staff(self, staff_member: Staff):
        """
        Adds a staff member object to the department.
        """
        self.staff.append(staff_member)


class Hospital:
    """
    The main class that contains and organizes departments.
    """
    def __init__(self, name: str, location: str):
        """
        Initialize a Hospital instance.
        :param name: Hospital name
        :param location: Hospital location
        """
        self.name = name
        self.location = location
        self.departments = [] # Aggregation of Department objects

    def add_department(self, department: Department):
        """
        Adds a department to the hospital.
        """
        self.departments.append(department)

    def display_hospital_summary(self):
        """
        Prints a summary of the hospital structure and resources.
        """
        print(f"\n{'='*10} {self.name} ({self.location}) {'='*10}")
        for dept in self.departments:
            print(f"Department: {dept.name}")
            print(f"  - Staff count: {len(dept.staff)}")
            print(f"  - Patient count: {len(dept.patients)}")


# --- System Demonstration ---
if __name__ == "__main__":
    # 1. Create Hospital
    my_hospital = Hospital("City Care Clinic", "Central District")

    # 2. Create Departments
    cardio = Department("Cardiology")
    ortho = Department("Orthopedics")

    # 3. Add Departments to Hospital
    my_hospital.add_department(cardio)
    my_hospital.add_department(ortho)

    # 4. Create Staff and Patients
    doc = Staff("Dr. Ali", 35, "Surgeon")
    pat = Patient("Yasser", 28, "Stable Condition")

    # 5. Assign them to a Department
    cardio.add_staff(doc)
    cardio.add_patient(pat)

    # 6. Display Results
    print(doc.view_info())
    print(pat.view_record())
    my_hospital.display_hospital_summary()
from abc import ABC, abstractmethod

class Doctor(ABC):    
    @abstractmethod
    def treat(self):
        pass

class Surgeon(Doctor):
    def treat(self):
        print('Метод личения Surgeon')

class Dentist(Doctor):
    def treat(self):
        print('Метод личения Dentist')

class Therapist(Doctor):
    def treat(self):
        print('Метод личения Therapist')

    def add_doctor(self, patient):
        if patient.treatment_plan == 1:
            patient.doctor =  Surgeon()
        elif patient.treatment_plan == 2:
            patient.doctor =  Dentist()
        else:
            patient.doctor = Therapist()

        print(f"Пациенту: {patient.name} назначен {patient.doctor.__class__.__name__}")
        patient.doctor.treat()

class Patient:
    def __init__(self, name, treatment_plan):
        self.name = name
        self.treatment_plan = treatment_plan
        self.doctor = None

therapist = Therapist()

p1 = Patient("Иван", 1)
therapist.add_doctor(p1)

print()

p2 = Patient("Сергей", 2)
therapist.add_doctor(p2)

print()

p3 = Patient("Олег", 5)
therapist.add_doctor(p3)
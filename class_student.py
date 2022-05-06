class Details:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Study:
    def __init__(self, semester: int):
        self.semester = semester


class Student:
    def __int__(self, details: Details, studies: Study):
        self.details = details
        self.studies = studies



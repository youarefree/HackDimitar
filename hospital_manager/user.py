from hashing import validate_pass


class User:

    def __init__(self):
        self.username = None
        self.password = None
        self.age = None
        self.gender = None

    def initialise(self, username, password, age, gender):
        self.username = username

        if validate_pass(password):
            self.password = password
        else:
            return False
        self.age = age
        if self.validate_gender(gender):
            self.gender = gender
        return True

    def validate_gender(self, gender):
        if gender not in ["Male", "Female", 'male', 'female', 'm', 'f']:
            print("Not a recognised gender")
            return False
        return True


class Doctor(User):

    def __init__(self):
        super().__init__()

    def initialise(self, title):
        self.title = title

    def __str__(self):
        return super().__str__ + "is a {}".format(self.title)

    def __repr__(self):
        return self.__str__


class Patient(User):
    def __init__(self):
        super().__init__()

    def initialise(self, doctor_id):
        self.doctor_id = doctor_id

    def __str__(self):
        return super().__str__ + "is taken a patient"

    def __repr__(self):
        return self.__str__

    def get_doctor(self, id):
        pass

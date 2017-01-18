from hashing import validate_pass


class User:

    def __init__(self):
        self.username = None
        self.password = None
        self.age = None
        self.gender = None

    def initialise(self, username, password):
        self.username = username

        if validate_pass(password):
            self.password = password
        else:
            return False

class Client:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email
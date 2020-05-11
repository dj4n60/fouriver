# here we have the classes of the user types (customers,developers or system admins)

class User:
    def __init__(self, first_name, last_name, password, idiotita):
        self.username = username
        self.first_name = name
        self.last_name = last_name
        self.password = password
        self.idiotita = idiotita


    def searchprofile(self):
        print('test')

    def comment(self):
        print('test')

    def review(self):
        print('test')

    def recommend(self):
        print('test')


class Customer(User):
    idiotita = "customer"

    def createproject(self):
        print('test')

    def assign(self):
        print('test')


class Developer(User):
    type = "developer"

    def acceptproject(self):
        print('test')


class Admin(User):
    idiotita = "admin"

    def deleteuser(self):
        print('test')

    def deleteproject(self):
        print('test')

# here we have the classes of the user types (customers,developers or system admins)

class User:
    username = ""
    password = ""
    birthday = ""

    def searchprofile(self):
        print('test')

    def comment(self):
        print('test')

    def review(self):
        print('test')

    def recommend(self):
        print('test')


class Customer(User):
    type = "customer"

    def createproject(self):
        print('test')

    def assign(self):
        print('test')


class Developer(User):
    type = "developer"

    def acceptproject(self):
        print('test')


class Admin(User):
    type = "admin"

    def deleteuser(self):
        print('test')

    def deleteproject(self):
        print('test')
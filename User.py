class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    #los metodos necesitan self en su argumento obligatoriamente
    def getInfo(self):
        print(f'Nombre: {self.age}, Edad: {self.age}, correo: {self.email}')

from User import User

print("hello world")

name = 'Cesar'
print(name)

number1 = 1
print(number1)

#variable2 = variable1 + num (esto da error) no puedes sumar string con int, solo strings.
#print(variable2)

if 4 < 2:
    print("is minor")
else:
    print("is not minor")

vector1 = ["joel", "eliud", "ana", "la otra ana", "pancho", "karen", "pablito"]

print(vector1)

print(vector1[0])

movies = ["the warrios", "amores perros", "toy story", "rata touille", "robert pattison te odio"]

print(movies)

for m in movies:
    m = m + " (clisificacion: R)"
    print(m)

#las funciones no necesitan self en su argumento
def showName():
    print('nombre perron: Jesus')

user1 = User("Pancho", 40, "waifuhunter@gmail.com")
print(user1.name)
user1.getInfo()

showName()
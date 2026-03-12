from faker import Faker
import random
# Import Faker y random

# Inicializamos Faker en español
fake = Faker("es_ES")
usuarios_faker = {}

# Creamos diccionario vació donde posteriormente agregaremos los nombres generados

# Creeamos un bucle para rellenar el diccionario con los 15 usuarios
for us in range(1, 16):
    usuarios_faker[us] = {
        "Nombre": fake.name(),
        "Dirección": fake.address().replace(
            "\n", ", "
        ),  # Resultado Direccion busca salto de linea y reemplaza por una coma y un espacio
        "Email": fake.email(),
        "Teléfono": fake.phone_number(),
    }

print("--Lista de usuarios--")
# Al ser diccionario buscamos iterar por sus claves y para eso debemos usar .items()
for id, info in usuarios_faker.items():
    print(f"Id:{id}")
    print(f"Nombre: {info['Nombre']}")
    print(f"Dirección: {info['Dirección']}")
    print(f"Email: {info['Email']}")
    print(f"Teléfono: {info['Teléfono']}")
    print(
        "-" * 20
    )  # para separa la informacion de cada usuario repita al final un guion 10 veces

# Generamos usuario aletoriomente

id_aleatorio = random.randint(1, 15)

nombre_afortunado = usuarios_faker[id_aleatorio]["Nombre"]

print(f"O usuario chamado {nombre_afortunado} foi o afortunado!")


import pandas as pd # type: ignore
import random
from faker import Faker # type: ignore

fake = Faker()
data = []

for _ in range(200):
    record = {
        'ID': _ + 1,
        'Nombre': fake.first_name(),
        'Apellido': fake.last_name(),
        'Edad': random.randint(18, 65),
        'Género': random.choice(['Masculino', 'Femenino']),
        'Tipo de Seguro': random.choice(['Auto', 'Salud', 'Hogar', 'Vida']),
        'Prima Mensual': round(random.uniform(50, 500), 2),
        'Fecha de Inicio': fake.date_between(start_date='-5y', end_date='today'),
        'Estado': random.choice(['Activo', 'Cancelado', 'En Espera']),
    }
    data.append(record)

df = pd.DataFrame(data)
df.to_excel('datos_seguros.xlsx', index=False)

print('hola')
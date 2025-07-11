from faker import Faker
import pandas as pd

fake = Faker('pt_BR')  # para dados brasileiros

# Quantidade de registros
num_registros = 10

# Criando listas para cada coluna
nomes = [fake.name() for _ in range(num_registros)]
datas = [fake.date_between(start_date='-1y', end_date='today') for _ in range(num_registros)]
emails = [fake.email() for _ in range(num_registros)]
telefones = [fake.phone_number() for _ in range(num_registros)]

# Criando DataFrame
df = pd.DataFrame({
    'Nome': nomes,
    'Data': datas,
    'Email': emails,
    'Telefone': telefones
})

# Salvando em Excel
df.to_excel('fake_data.xlsx', index=False)

print("Arquivo 'fake_data.xlsx' gerado com sucesso!")

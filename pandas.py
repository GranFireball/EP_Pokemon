import pandas as pd

# Carrego o arquivo json do scrap e salvo em um DataFrame
df = pd.read_json("pokemons_info.txt", lines=True)
#print(df)

# Verifico se existem Nulos no DataFrame, no nosso caso não tem nenhum
print(df.isna().sum())

# Processo realizado em Excel
# A coluna tipo_dano transformada em colunas separadas
df2 = pd.read_csv("pokemon_danos.csv", sep=';')

# Removo a coluna tipos_dano do arquivo orignal
df.drop('tipos_dano', axis=1, inplace=True)

# Faço um junção do arquivo original com o arquivo formatado
df = pd.concat([df, df2], axis=1)
print(df)

# Salvo o arquivo final em csv
df.to_csv('append.csv', encoding='utf-8')

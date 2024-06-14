import pandas as pd

df = pd.read_csv('full.csv')


def extrair_primeiro_nome(nome):
    if ',' in nome:
        partes = nome.split(',')
        primeiro_nome = partes[1].strip().split()[1]
    else:
        primeiro_nome = nome.split()[2]
    return primeiro_nome


df['Primeiro Nome'] = df['Name'].apply(extrair_primeiro_nome)

primeiros_nomes_mais_comuns = df.groupby(['Pclass', 'Primeiro Nome']).size().reset_index(name='Quantidade')
primeiros_nomes_mais_comuns = primeiros_nomes_mais_comuns.sort_values(['Pclass', 'Quantidade'], ascending=[True, False])
primeiros_nomes_mais_comuns = primeiros_nomes_mais_comuns.drop_duplicates('Pclass')

print(primeiros_nomes_mais_comuns)

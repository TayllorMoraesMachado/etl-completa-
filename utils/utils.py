import pandas as pd


def printSchema(df):
    for coluna in df.columns:
        print(f'{coluna}: {df[coluna].dtype}')

def create_table_bronze(df,nome_tabela, engine, schema):
    df.to_sql(nome_tabela, con=engine, schema=schema, if_exists='append', index=False)
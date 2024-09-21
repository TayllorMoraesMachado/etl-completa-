import pandas as pd 


#### Importando classes
from utils.extract import Extract
##################################


#### Definindo o valor das váriaveis 
key = '88378df40a7ab0fb352a3043054bc006'
page = 1
page_final = 2
dados = []

#### Declarando a classe
exec = Extract(key)

while page <= page_final:
    print(f'Procurando os identificadores de filmes da página {page}')

    movie_ids = exec.get_movies(page)
    for movie_id in movie_ids:
        print(f'Procurando os detalhes do filme ID {movie_id}')
        movie_details = exec.get_movie_details(movie_id)
        dados.append(movie_details)
    page +=1 
   
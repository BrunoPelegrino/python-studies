import json
import csv

# carregar o arquivo JSON
with open('arquivo.json') as f:
    livros = json.load(f)

# calcular a quantidade de livros em cada categoria
total_livros = len(livros)
categorias = {}
for livro in livros:
    for categoria in livro['categories']:
        if categoria not in categorias:
            categorias[categoria] = 0
            categorias[categoria] += 1

# calcular a porcentagem de livros em cada categoria
porcentagens = {}
for categoria, quantidade in categorias.items():
    porcentagem = quantidade / total_livros * 100
    porcentagens[categoria] = round(porcentagem, 2)

# escrever os resultados em um arquivo CSV
with open('resultados.csv', mode='w') as f:
    writer = csv.writer(
        f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
    writer.writerow(['Categoria', 'Porcentagem'])
    for categoria, porcentagem in porcentagens.items():
        writer.writerow([categoria, porcentagem])

filmes = ["Vingadores", "Liga da justiça", "Power"]
jogos = ["God of war", "Minecraft", "Portal"]
livros = ["O alquimista", "Harry Potter", "O Senhor dos Anéis"]
esporte = ["Futebol", "Basquete", "Volei"]

#A)
listas = [filmes, jogos, livros, esporte]

print("Lista de filmes: ", filmes)
print("Lista de jogos: ", jogos)
print("Lista de livros: ", livros)
print("Lista de esportes: ", esporte)
print("Lista que contém todas as listas:", listas)

#B)
print("Um dos itens da lista de livros:", livros[2])

#C)
listas.append(["Linguagem de Programação", "IOT", "Modelagem de Dados"])
print("Lista que contém todas as listas atualizada com a lista 'Disciplinas': ", listas)
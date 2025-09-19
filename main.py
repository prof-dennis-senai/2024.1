# Lista - mutável
lista_compras = ['arroz', 'feijao', 'macarrao', 'batata']
print(lista_compras)
lista_compras.append("Maça")
print(lista_compras)


# Tuplas - imutável
tupla_alunos = ("Joao", "Maria", "Pedro")
print(tupla_alunos)
# tupla_alunos.append('Marcos')

print(lista_compras.pop())
print(lista_compras)


# Dicionários - mutável
dicionario_alunos = {
    "Joao": 10,
    "Maria": 8,
    "Pedro": 7
}
print(dicionario_alunos)

dicionario_alunos["Ricardo"] = 10
print(dicionario_alunos)

print(dicionario_alunos["Ricardo"])
print(dicionario_alunos.get("Ricardo"))

print(dicionario_alunos.items())


print('---------------')
lista_unidades = [('Joao', 10), ('Maria', 8), ('Pedro', 7), ('Ricardo', 10)]

print(lista_unidades)

dicionario_unidade = dict(lista_unidades)
print(dicionario_unidade)
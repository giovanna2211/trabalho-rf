cmarcos = 0
cjuliana = 0
cjoao = 0
votosbrancos = 0
votosnulos = 0
voto = 0

while voto != 6:
    print("As opções são:")
    print("1. Candidata Juliana")
    print("2. Candidato Marcos")
    print("3. Candidato João")
    print("4. Nulo")
    print("5. Branco")
    print("6. Encerrar votação")

    voto = int(input("Vote: "))

    if voto == 2:
        cmarcos = cmarcos + 1
    elif voto == 1:
        cjuliana = cjuliana + 1
    elif voto == 3:
        cjoao = cjoao + 1
    elif voto == 5:
        votosbrancos = votosbrancos + 1
    elif voto == 4:
        votosnulos = votosnulos + 1
    else:
        print("Opção inválida")

totalvotos = cjuliana + cmarcos + cjoao + votosnulos + votosbrancos
pbrancos = (votosbrancos / totalvotos) * 100
pnulos = (votosnulos / totalvotos) * 100


if cjoao > cjuliana and cjoao > cmarcos:
    vencedor = "Candidato João"
elif cmarcos > cjuliana and cmarcos > cjoao:
    vencedor = "Candidato Marcos"
elif cjuliana > cmarcos and cjuliana > cjoao:
    vencedor = "Candidata Juliana"
else:
    vencedor = "Empate"

print(f"Número de votos de Candidata Juliana: {cjuliana}")
print(f"Número de votos de Candidato Marcos: {cmarcos}")
print(f"Número de votos de Candidato João: {cjoao}")
print(f"Porcentagem de votos brancos: {pbrancos:.2f}%")
print(f"Porcentagem de votos nulos: {pnulos:.2f}%")
print(f"Candidato vencedor: {vencedor}")
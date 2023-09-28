qntnotas = int(input("Digite a quantidade de notas: "))
somapesos = 0
somanotas = 0
contador = 1

while contador <= qntnotas:
    nota = float(input(f"Informe a nota {contador}: "))
    peso = float(input(f"Informe o peso da nota {contador}: "))
    somapesos = somapesos + peso
    somanotas = somanotas + nota * peso
    contador += 1

if somapesos != 0:
    media_ponderada = somanotas / somapesos
    print(f"A média ponderada é: {media_ponderada:.1f}")
else:
   print("Não é possível calcular a média com peso zero.")
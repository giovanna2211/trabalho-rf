n = int(input("Informe um número: "))
soma = 0
contador = 1
print(f"Somar de {contador} até {n}: ")

while n >= contador:
    if contador % 2 == 0:
        soma = soma + contador
        contador = contador + 1
    else:
        contador = contador + 1
print(soma)=
n = int(input("Digite um número: "))
contador = 1
soma = 0

print(f"Somar de {contador} até {n}")

while n > contador:
    soma = soma + contador
    contador = contador + 1
print(soma + n)
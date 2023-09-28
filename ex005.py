n = int(input("Digite um número: "))
contador = 0

while n >= contador:
    if n % 2 == 0:
        print(n)
        n = n - 2
    else:
        n = n - 1
n = int(input("Digite um número: "))
contador = 1

while n >= contador:
    if n % 2 == 1:
        print(n)
        n = n - 2
    else:
        n = n - 1
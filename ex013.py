np = int(input("Quantos produtos você deseja comprar (até 5)? "))
totalc = 0
contador = 0

if np <= 5:  
    while contador < np:
        np = input(f"Nome do Produto {contador + 1}: ")
        quantidade = int(input(f"Quantidade do Produto {contador + 1}: "))
        valoru = float(input(f"Valor Unitário do Produto {contador + 1}: "))
        valorttp = quantidade * valoru
        totalc = totalc + valorttp
        print(f"Valor Total do Produto {contador + 1}: R${valorttp:.2f}")
        contador = contador + 1
    print(f"Valor Total das Compras: R${totalc:.2f}")
else:
    print("Desculpe, você pode comprar até 5 produtos.")

contador = "S"

while contador =="S":
  num1 = int(input("Digite o primeiro número: "))
  num2 = int(input("Digite o segundo número: "))
  soma = num1 + num2
  print(f"{num1} + {num2} = {soma}")
  contador = input("Deseja realizar mais uma soma? [S ou N]: ")
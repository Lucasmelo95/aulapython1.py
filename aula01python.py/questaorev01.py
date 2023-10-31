num1 = int(input("Digite um numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 > num2:
    print(f"O primeiro numero é maior! *{num1}*")
elif num2 > num1:
    print(f"O segundo numero é maior! *{num2}*")
else:
    print("Os numeros são iguais")
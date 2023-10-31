nome = str(input("Digite um nome:"))
contador = 0

for letra in nome:
    if letra.lower() == "a":
        contador += 1
        print(f"O nome {nome} tem {contador} letras 'a'")

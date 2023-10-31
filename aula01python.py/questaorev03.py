sexo = str(input("Digite [ M ] para Masculino ou [ F ] para Feminino :")).upper().strip()

if len(sexo) == 1:
    if sexo =="M": 
        print("Sexo Masculino")
    elif sexo == "F":
        print("Sexo Feminino")
    else:
        ("Sexo invalido !")
else:
    print("Digite apenas uma letra")
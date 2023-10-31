cor = str(input("Escolha uma cor do semáforo: ")).lower()

match cor:
    case "vermelho":
        print("Pare!")
    case "amarelo":
        print("Atenção!")
    case "verde":
        print("Acelere!")
    case _:
        print("Cor inválida")
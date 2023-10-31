cor = int(input("""
                Escolha uma cor do semáforo:
                1 - Vermelho
                2 - Amarelo
                3 - Verde
                 """))
match cor:
    case 1:
        print("Pare!")
    case 2:
        print("Atenção!")
    case 3:
        print("Acelere!")
    case _:
        print("Cor inválida")
while True:
    cor = str(input("Digite uma cor do semaforo: ")).lower()


    if cor == "vermelho":
      print("Pare !")
      break

    if cor == "amarelo":
      print("Atenção !")
      break

    if cor == "verde":
      print("Acelere !")
      break

    else:
      print("Cor inválida, Digite outra Cor")
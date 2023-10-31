nota1 = float(input("Digite uma nota :"))
nota2 = float(input("Digite a segunda nota :"))
nota3 = float(input("Digite a terceira nota :"))
nota4 = float(input("Digite a quarta nota :"))

soma = (nota1 + nota2 + nota3 + nota4) / 4

if soma >= 7 and soma < 10:
    print("Aluno aprovado!")
elif soma < 7 and soma <= 0:
    print("Aluno Reprovado!")
elif soma == 10:
    print("Aprovado com distinçao")
else:
    print("Media invalida, digite notas entre 0 e 10 ")
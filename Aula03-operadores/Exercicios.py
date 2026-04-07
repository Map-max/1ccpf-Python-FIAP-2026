

# Exercicio 2 --- Ímpar ou Par

def imp_ou_par():
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")

# Execicio 3 --- Maior ou Menor

def maior_ou_menor(num1, num2):
    num1 = int(input("Digite o numero: "))
    num2 = int(input("Digite o numero: "))
    if num1 == num2:
        print("Eles são iguais")

    else:
        if num1 > num2:
            print(f"{num1} é mair que {num2}.")

        else:
            print(f"{num2} é maior que {num1}.")

# Exercicio 4 --- Media

def media_da_nota(num1, num2, num3, num4, media):
    num1 = int(input("Digite a nota 1:"))
    num2 = int(input("Digite a nota 2:"))
    num3 = int(input("Digite a nota 3:"))
    num4 = int(input("Digite a nota 4:"))

    media = (num1 + num2 + num3 + num4)/4

    if media >= 6:
        print("Aprovado")
    elif media >= 5 :
        print("recuperação")
    else:
        print("Reprovado")

# Exerciocio 5 --- Multipos


def main():
    opcoes = {
            1: imp_ou_par,
            2: maior_ou_menor,
            3: media_da_nota
        }

        print("1 - Ímpar ou Par")
        print("2 - Maior ou Menor")
        print("3 - Média")

        escolha = int(input("Escolha: "))

        funcao = opcoes.get(escolha)

        if funcao:
            funcao()  # 🔥 chama automaticamente
        else:
            print("Opção inválida")


main()
# Fim

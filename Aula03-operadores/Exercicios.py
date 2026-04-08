# Exercícios de Operadores

# Exercicio 1 --- Audio Mp3

def audio_mp3():
    import subprocess
    import os
    
    # Get the directory of this script and navigate to assets folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_audio = os.path.join(script_dir, "..", "assets", "Duran Duran - invisible Metal Gear Version [RoYXgdHafBA].mp3")
    
    subprocess.Popen(["wmplayer.exe", caminho_audio])
    print("Reproduzindo áudio...")

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
            print(f"{num1} é maior que {num2}.")

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
            1: audio_mp3,
            2: imp_ou_par,
            3: maior_ou_menor,
            4: media_da_nota
        }

    print("1 - Audio Mp3")
    print("2 - Ímpar ou Par")
    print("3 - Maior ou Menor")
    print("4 - Média")

    escolha = int(input("Escolha: "))

    funcao = opcoes.get(escolha)

    if funcao:
        funcao()  
    else:
        print("Opção inválida")


main()
# Fim

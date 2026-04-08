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

def media_da_nota():
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
def multiplos():
    num1 = int(input("Digite o numero: "))
    num2 = int(input("Digite o numero: "))

    if num1 % num2 == 0:
        print(f"{num1} é múltiplo de {num2}.")
    else:
        print(f"{num1} não é múltiplo de {num2}.")

# Exercicio 6 --- Calculadora
def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    if operacao == "+":
        print(f"Resultado: {num1 + num2}")
    elif operacao == "-":
        print(f"Resultado: {num1 - num2}")
    elif operacao == "*":
        print(f"Resultado: {num1 * num2}")
    elif operacao == "/":
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
# Exercício 7 --- Votação
def votacao(idade):
    idade = int(input("Digite a sua idade: "))

    if idade < 16:
        print("Não pode votar")
    elif 16 <= idade < 18 or idade >= 70:
        print("Voto opcional")
    else:
        print("Voto obrigatório")

# Exercício 8 --- Salário
def salario():
    salario = float(input("Digite o salário: "))

    if salario <= 280:
        aumento = salario * 0.20
    elif salario <= 700:
        aumento = salario * 0.15
    elif salario <= 1500:
        aumento = salario * 0.10
    else:
        aumento = salario * 0.05

    novo_salario = salario + aumento
    print(f"Salário antes do aumento: {salario:.2f}")
    print(f"Percentual de aumento aplicado: {aumento/salario*100:.0f}%")
    print(f"Valor do aumento: {aumento:.2f}")
    print(f"Novo salário: {novo_salario:.2f}")

# Pulei o exercício 9

# Exercício 10 --- Identificação de Triângulos
'''
Se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO;
▪ Se A² = B² + C² , apresente a mensagem: TRIANGULO RETANGULO;
▪ Se A² > B² + C² , apresente a mensagem: TRIANGULO OBTUSANGULO;
▪ Se A² < B² + C² , apresente a mensagem: TRIANGULO ACUTANGULO

'''
def identificacao_triangulos():
    lado1 = float(input("Digite o lado 1: "))
    lado2 = float(input("Digite o lado 2: "))
    lado3 = float(input("Digite o lado 3: "))

    # Sort the sides so we can check them properly
    # This puts the smallest side first, largest last
    lados = sorted([lado1, lado2, lado3])
    a, b, c = lados  # a is smallest, c is largest

    # Check if it can form a triangle
    # For a triangle, the sum of any two sides must be bigger than the third side
    # Since we sorted, we only need to check if a + b > c
    if a + b <= c:
        print("NAO FORMA TRIANGULO")
    else:
        # It forms a triangle, now check the angles
        # Use the largest side (c) as the hypotenuse
        if c**2 == a**2 + b**2:
            print("TRIANGULO RETANGULO")
        elif c**2 > a**2 + b**2:
            print("TRIANGULO OBTUSANGULO")
        else:
            print("TRIANGULO ACUTANGULO")

        # Check if sides are equal
        if a == b == c:
            print("TRIANGULO EQUILATERO")
        elif a == b or b == c or a == c:
            print("TRIANGULO ISOSCELES")

def main():
    opcoes = {
            1: audio_mp3,
            2: imp_ou_par,
            3: maior_ou_menor,
            4: media_da_nota,
            5: multiplos,
            6: calculadora,
            7: votacao,
            8: salario,
            10: identificacao_triangulos
        }

    print("1 - Audio Mp3")
    print("2 - Ímpar ou Par")
    print("3 - Maior ou Menor")
    print("4 - Média")
    print("5 - Múltiplos")
    print("6 - Calculadora")
    print("7 - Votação")
    print("8 - Salário")
    print("9 - (Pulei o exercício 9)")
    print("10 - Identificação de Triângulos")

    escolha = int(input("Escolha: "))

    funcao = opcoes.get(escolha)

    if funcao:
        funcao()  
    else:
        print("Opção inválida")
main()
# Fim
# Exercicios de repetição
from nltk.corpus import comtrans
from numba.cpython.randomimpl import np_log_normal_impl1


# Numero 1 --- ola mundo
def escolha_simples():
    while True:
        print("Hello world")
        print("deseja repitir o ultimo comando?")
        var = input("responda com sim ou não (s ou n):")
        if var == "s" :
            continue
        elif var == "n" :
            break
# Exer num 2 --- contagem de 10 em 10 até 100

def contagem_ate_cem():
    num_1 = 0
    while num_1 <= 100:
        print(num_1)
        num_1 += 10

# Exer num 3 --- tabuada de um numero x até 10

def tabuada():
    num1 = int(input("Digite um número: "))
    for mult in range(1, 11):
        print(f"{num1} x {mult} = {num1 * mult}")

# Exer num 4 --- soma de 5 valores imformado pelo usuario

def soma_de_5():
    soma = 0
    for i in range(1,6):
        num1 = int(input("digite um valor:"))
        soma += num1
    print(f"A soma dos valores é :{soma}")

# Exer 5 --- pegar 5 valores e ver qual é o maior

def maior_ou_menor():
    num1 = 0
    for i in range(1, 6):
        num2 = int(input("digite um valor:"))
        if num2 > num1:
            num1 = num2
    print(f"Este é o maior valor:{num1}")

# Exer 6 --- mostrar valores pares de 2 até um valors informado pelo usuario

def valores_pares():
    n = int(input("\nDigite o valor limite: "))

    print(f"\nNúmeros pares entre 2 e {n}:")
    for i in range(2, n + 1, 2):
        print(i)

# Exer 7 --- fatorial so que soma

def fac_soma():
    num2 = 0
    num1 = int(input("\ndigite o valor final:"))
    while num1 <= 0:
        print("\nO valor precisa ser positivo")
        num1 = int(input("digite o valor novamente:"))
    for i in range(1, num1 + 1):
        num2 += i
        print(i)
    print(f"\nSoma de todos os acima valores até {num1} é\n")
    print(f"Resposta:{num2}")

# Exer 8 --- cansei de ficar escrevendo esses coemtarios, vou parei aqui

def divisores():
    num = int(input("valor final:"))
    for i in range(1, num + 1):
        if (num % i) == 0:
            print(f"{i} é um divisor de {num}")

def primos():
    print("Números primos entre 2 e 2000:\n")

    for n in range(2, 2001):
        primo = True
        for i in range(2, n):
            if n % i == 0:
                primo = False
                break
        if primo:
            print(n)
def main():
    opcoes = {
            1: escolha_simples,
            2: contagem_ate_cem,
            3: tabuada,
            4: soma_de_5,
            5: maior_ou_menor,
            6: valores_pares,
            7: fac_soma,
            8: divisores,
            9: primos
        }

    print("1 - escolha simples")
    print("1 - comtagem ate cem")
    print("3 - tabuda")
    print("4 - soma_de_5")
    print("5 - maior ou menor")
    print("6 - valores pares")
    print("7 - fatorial so que soma")
    print("8 - divisores")
    print("9 - primos")

    escolha = int(input("Escolha: "))

    funcao = opcoes.get(escolha)

    if funcao:
        funcao()
    else:
        print("Opção inválida")
main()
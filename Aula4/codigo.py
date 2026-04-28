# Exercicios de repetição

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


def main():
    opcoes = {
            1: escolha_simples,
            2: contagem_ate_cem,
            3: tabuada,
            4: soma_de_5
        }

    print("1 - escolha simples")
    print("1 - comtagem ate cem")
    print("3 - tabuda")
    print("5 - soma_de_5")
    escolha = int(input("Escolha: "))

    funcao = opcoes.get(escolha)

    if funcao:
        funcao()
    else:
        print("Opção inválida")
main()
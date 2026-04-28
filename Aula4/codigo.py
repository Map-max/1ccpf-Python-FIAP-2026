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

def main():
    opcoes = {
            1: escolha_simples,
            2: contagem_ate_cem
        }

    print("1 - escolha simples")
    print("1 - comtagem ate cem")

    escolha = int(input("Escolha: "))

    funcao = opcoes.get(escolha)

    if funcao:
        funcao()
    else:
        print("Opção inválida")
main()
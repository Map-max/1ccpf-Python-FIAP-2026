#função com parametro sem retorno
def boas_vindas(nome):
    print(f"olá, {nome}! Seja bem vindo!")

nome_digitado = input("digite seu nome:")
boas_vindas(nome_digitado)

#Função com retorno
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado = soma(4, 3)
print(f"Resultadoo:{resultado}")
print(type(soma))
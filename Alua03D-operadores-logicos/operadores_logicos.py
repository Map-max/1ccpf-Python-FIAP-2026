from sympy import false

verifica_email = True
verifica_senha = True

verifica_login =  verifica_email and verifica_senha
print(verifica_login)

logica_ou = False or False or True
print(logica_ou)

negação = not False
print(negação)

if not verifica_login:
    print("digita certo")
else:
    print("entra progrma")
import random
import string
caracteres = string.ascii_letters,string.digits
def gerar_senha():
    senha = ''
    for i in range(12):
        senha += random.choice(caracteres)
        return senha
    gerar_senha()
nova_senha = gerar_senha()
print(nova_senha)

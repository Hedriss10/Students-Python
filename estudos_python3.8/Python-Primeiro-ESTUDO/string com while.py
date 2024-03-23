# indices
#   0123456789.................32

#interação <- interar
frase = 'Dinheiro não é tudo'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
#while contador < 10:
    #print(frase[contador], contador)
     #nova_string += frase[contador]
     #print(nova_string)

     #contador += 1

#print(nova_string)

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'R':
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
        contador += 1

print(nova_string)

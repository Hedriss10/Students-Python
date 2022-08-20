"""
sistema de validação de aposentadoria completo e com cadastro 

"""


print("\nSeja bem vindo o sistema de aposentadoria\n")


nome = input("\nQual é o seu nome\n")
sobrenome = input("\nQual é seu sobrenome\n")
print(f'Seja bem vindo {nome} {sobrenome}')
idade = input("\nDigite a sua idade:\n")
sexo = input("\nDigite o seu sexo, (M , para masculino  e F, para feminino)\n")


if sexo.upper() == 'M':
    if int(idade) >=65:
     print("\nParabéns você está aposentado!\n")
    else:
        print("\nVocê não tem a idade permitida para aposentadoria\n")
elif sexo.upper() == 'F':
    if int(idade) >= 65:
        
     print("Parabéns você está aposentada!")
    else:
        print("Você não tem idade permitida para aposentadoria ")
else:
    print("Você digitou alguma opção invalida por favor tente novamente..")
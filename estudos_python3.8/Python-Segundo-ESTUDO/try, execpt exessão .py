try
    A= []

except NameError as erro:
    print('Aconteceu um erro com á maquina, por favo verifique seu computador.')
except (ConnectionError, KeyError) as erro:
    print('Erro de conexão e também de chave.')
except Exception as erro:
    print('Ocorreu um erro inesperador')
else:
    print('Seu código foi executado com sucesso')
    print(a)
finally:
    print('Graças á Deus.')

print(input('Bora continuar?'))

print(A)


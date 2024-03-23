"""
    erros
    são otimos para testes
    são realizados para dar um stop em determinado local de code
    e podemos passa uma mensagem costumizada quando o erro aparece
"""
from random import randint


try:
    print('Números sorteados, escolhe o seu e boa sorte')
    numero = int(input("\nMe fala um número de 0 á 10: \n"))

    numero_sorteado = 6
    numero_aleatorio = randint(0, 10)

    if numero == numero_sorteado:
        print("Parabéns você ganhou com multiplicador de 2x")
    else:
        print(f'Número sorteado da vez é o {numero_aleatorio}')

except:
    print('Você digitou um texto e jogo é composto de números')

finally:
    print(f'Tente novamente e boa sorte!')


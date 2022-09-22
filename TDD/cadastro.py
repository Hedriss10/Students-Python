"""
1 = Receber um número inteiro
2 = Saber se o número é multiplo de 3 e 5:
    Aprovados
3 = Saber se o número é multiplo somente de 3:
    Reprovados
4 = Saber se o número é multiplo somente de 5:
    Cadastrados  
5 = Saber ser o número NÃO é multiplo de 3 e 5 :
    Aceitos
""" 



def logins_user_cadastrados(n):
    assert isinstance(n, int), 'n deve ser int'

    if n % 3 == 0 and n % 5 == 0:
        return 'Aprovados'

    if n % 3 == 0:
        return 'Aceitos'

    if n % 5 == 0:
        return 'Cadastrados'

    return 'Reprovados'
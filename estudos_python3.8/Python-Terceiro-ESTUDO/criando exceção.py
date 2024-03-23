class TaErradoErro(Exception):
    pass


def testar():
    raise TaErradoErro('Está errado')

try:
    testar()
except TaErradoErro as error:
    print(f'Erro: {error}')







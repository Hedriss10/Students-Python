

def lista_de_clientes(clientes_iteravel, lista=[]):
    lista.extend(clientes_iteravel)
    return lista


clientes1 = lista_de_clientes(['Hedris', 'Hernque', 'brancao'])
clientes2 = lista_de_clientes(['joão', 'vida', 'vai toma no cu'])

print(clientes1)
print(clientes2)

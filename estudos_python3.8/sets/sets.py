"""
    Set(listas)
    similar a listas
    evitar itens duplicados
    não utiliza index
    | = é igual unificação de duas listas para a determinação da tomada de decisão

    - =  Difference de um set

    ^ = Symmetric Difference

    & = And

    len = United in vetores

"""


list1 = [10, 20, 100, 40, 50]

list2 = [10, 20, 30, 40, 70]


num1 = set(list1)

num2 = set(list2)


print(num1 | num2) # Union

print(num1 - num2) # Difference

print(num1 ^ num2) # Symmetric Difference

print(num1 & num2) # And


print(len(num1))

##print(list1)
##print(list2)
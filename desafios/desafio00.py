"""
    desafio do python para obter boas praticas 
"""


temperatura = int(input("\nQual é a temperatura da carne?\n"))

if temperatura < 48:
    print("Cozinhar por mais alguns minutos!")

elif temperatura in range(48, 53):
    print("Selada")
    
elif temperatura in range(54, 59):
    print("Ao ponto para mal")
    
elif temperatura in range(60, 64):
    print("Ao ponto")
    
elif temperatura in range(65, 70):
    print("Ao ponto para bem")
    
elif temperatura >= 71:
    print("Bem passada")    
    

else:
    print(f'Aconteuceu algum erro!')

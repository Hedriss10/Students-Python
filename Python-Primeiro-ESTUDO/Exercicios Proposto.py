 horario = input('Digite um horário (0-23): ')
 if horario.isdigit():
     horario = int(horario)

     if horario >= 0 and horario <= 23:
         if horario <= 11:
             print('Boa dia!')
         elif horario <= 17:
             print('Boa tarde!')
     else:
         print("Horário deve estar entre 0 e 23")
     else:
             print('Boa noite!')
 else:
     print("Por favor, digite um horário entre 0 e 23.")
print ('===========================================')
print ('==========PROJETO INTERDISCIPLINAR=========')
print ('===========================================')

print ('André dos Anjos - RGM: 25836048 \nArmando Victor - RGM:22034641 \nGiovanne Rodrigues - RGM: 26543877 \nMatheus Christovam - RGM: 25646222 \nVictor Oliveira - RGM: 26326957') 
cont = 1

binario=''
octadecimal=''
hexadecimal=''

print ('===========================================')
print ('Calculadora para Conversão de Decimal para:')
print ('=====Binário/ Octadecimal/ Hexadecimal=====')
print ('===========================================')

while cont == 1:

  num=int(input('Digite um Número Decimal: '))
  conv=int(input('[1] - Binário \n[2] - Octadecimal \n[3] - Hexadecimal \nEscolha: '))

# Validação Conversão
  if conv < 1 or conv > 3:
    print ('Digite um número válido')
  else:
    # BINARIO
    if conv==1:
      # Numero decimal
      if num < 0 or num == 0:
        print ('Favor digitar um número maior que zero')
      else: 
        while num!=0:
            r = num % 2 	
            binario = str(r) + binario 	
            num = num//2     	
        print('O decimal digitado equivale a %s na base 2.'%binario)

        cont = int(input('Deseja continuar? \n[1 - SIM] \n[2 - NÃO] \nEscolha: '))
        if cont < 1 or cont > 2:
          print ('Digite um número válido')
          cont = 1
          binario = ""
        else:
          if( cont == 1 ):
            cont = 1
            binario = ""
          else:
            cont = 2
            print('Obrigado por utilizar a calculadora')
            break
    # OCTAL
    elif conv==2:
      if num < 0 or num == 0:
        print ('Favor digitar um número maior que zero')
      else: 
        while num!=0:
            r = num % 8 	
            octadecimal = str(r) + octadecimal 	
            num = num//8
        print("O decimal digitado equivale a %s na base 8." %octadecimal)
        
        cont = int(input('Deseja continuar? \n[1 - SIM] \n[2 - NÃO] \nEscolha: '))
        if cont < 1 or cont > 2:
          print ('Digite um número válido')
          cont = 1
          octadecimal = ""
        else:
          if( cont == 1 ):
            cont = 1
            octadecimal = ""
          else:
            cont = 2
            print('Obrigado por utilizar a calculadora')
            break
    # HEXA
    elif conv==3:
      if num < 0 or num == 0:
        print ('Favor digitar um número maior que zero')
      else: 
        while num!=0:
            r = num % 16
            
            if(r == 10):
              trans = str(r).replace('10', 'A')
              hexadecimal = trans + hexadecimal

            elif(r == 11):
              trans = str(r).replace('11', 'B')
              hexadecimal = trans + hexadecimal

            elif(r == 12):
              trans = str(r).replace('12', 'C')
              hexadecimal = trans + hexadecimal
              
            elif(r == 13):
              trans = str(r).replace('13', 'D')
              hexadecimal = trans + hexadecimal
              
            elif(r == 14):
              trans = str(r).replace('14', 'E')
              hexadecimal = trans + hexadecimal
              
            elif(r == 15):
              trans = str(r).replace('15', 'F')
              hexadecimal = trans + hexadecimal

            else:
              hexadecimal = str(r) + hexadecimal 
            num = num//16 
        print("O decimal digitado equivale a %s na base 16." %hexadecimal)
        
        cont = int(input('Deseja continuar? \n[1 - SIM] \n[2 - NÃO] \nEscolha: '))
        if cont < 1 or cont > 2:
          print ('Digite um número válido')
          cont = 1
          hexadecimal = ""
        else:
          if( cont == 1 ):
            cont = 1
            hexadecimal = ""
          else:
            cont = 2
            print('Obrigado por utilizar a calculadora')
            break

            
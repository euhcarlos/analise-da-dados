resposta = input('Deseja usar a tabuada?(s/n): ')

if resposta.upper() == 'S':
  while(resposta.upper() == 'S'):
    operacao = input('Digite a operação (+, -, *, /) ou M para sair: ')
    if(operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/' or operacao == 'M'):

      if operacao == 'M':
        print('Até a próxima!')
        break

      numero1 = float(input('Digite o primeiro número: '))
      numero2 = float(input('Digite o segundo número: '))

      if(operacao == '+'):
        print(numero1 + numero2)

      elif(operacao == '-'):
        print(numero1 - numero2)

      elif(operacao == '*'):
        print(numero1 * numero2)

      elif(operacao == '/'):
        print(numero1 / numero2)

      resposta = input('Deseja continuar usando a tabuada?(s/n): ')
    else:
      print('Operação inválida!')
elif resposta.upper() == 'N':
    print('Até a próxima!')
else:
    print('Resposta inválida!')

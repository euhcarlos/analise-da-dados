# analise-da-dados

Como executar o calculando.sh?
Você tem duas maneiras de executar o calculando.sh, você pode clicar com o botão do lado direito do mouse e executar como programa e abrindo o local do arquivo no terminal e digitando "./calculando.sh"

Como foi feito o codigo da calculadora?
Em primeiro lugar, capturei o texto do usuário com a resposta S (indicando que ele quer usar a calculadora) e N (indicando que ele deseja sair da calculadora). Fiz uma condicional verificando qual a escolha do usuário, deixando todo o texto da resposta em maiúsculo, para que não haja necessidade de verificar S maiúsculo e s minúsculo, já transformando a resposta em maiúsculo e só comparando. Usei um loop while para continuar a execução do programa enquanto a resposta do usuário for S. Após isso, capturo qual operação o usuário gostaria de usar, usando o input. Depois, faço uma verificação para ver se a operação foi válida e saio do programa se for digitado M. Após, peço para que o usuário digite um número e, em seguida, digite outro. Com isso, faço condicionais para verificar qual operação foi escolhida e realizo a operação conforme a escolha do usuário. No final, pergunto se o usuário deseja continuar a usar a calculadora ou simplesmente parar. Se optar por parar, retorno uma mensagem de despedida; se desejar continuar, o loop reinicia.

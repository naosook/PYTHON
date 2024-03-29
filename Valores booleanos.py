Usamos uma instrução if para escrever o código que responda a diferentes situações. Nós o reconhecemos pela palvra-chave if.

if: True 
print("Hello")

A instrução if executa o código somente se for avaliado como verdadeiro. É como dizer, se algo é verdadeiro, faça isso. Vamos tornar a avaliação verdadeira simplesmente usando o valor booleano “True” para exibir "Hello" no console. Ex:

if True:
  print("Hello")
 
Programas inteligentes usam booleanos para tomar decisões sobre executar linhas de códigos ou ignorá-las.
Caso quisermos pular o código, precisamos que a afirmação seja avaliada como falsa. Vamos facilmente fazer com que a declaração seja avaliada como falsa simplesmente usando o valor booleano "False". Nada será impresso. Ex:

if False:
  print("Hello")
  
Valores como "True" são chamados de condições. Declarações que dependem de condições são chamadas de condicionais. As condições decidem se o código é executado ou ignorado. eles ficam entrem if e os dois pontos. Ex:

If True:
   print("Farinha e dois ovos, por favor")
   
As instruções if não decidem pular ou executar o código inteiro. Eles só tomam decisões sobre um bloco de código.
Em vez de usar o booleano True, podemos salvá-lo em uma variável como greet e usá-lo como condição. Ex:

greet = True 
if greet:
   print("Hello!")
   
Se caso a variável greet fosse definida como False, a mensagem seria ignorada.

O que esse código exibe no console?

is_online = True 
if is_online:
  print("Jill is online") #será exibido: Jill is online, pois a variável é "True"
  
O que esse código exibe no console:

inbox_full = False 
if inbox_full:
  print("Your inbox is full") #Nada porque a condição é avaliada como falsa
  
Podemos usar operadores de comparação em programas como Trivia App para verificar se a "answer" a uma pergunta está correta. Digite == neste programa para comparar a solução esperada com a resposta dada.

answer = "Picasso"
if answer == "Picasso"
  print(answer + "is correct!") #saída: Picasso is correct!
  


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

  Já vimos antes que variáveis também podem armazenar números. Ao contrário das strings, os valores numéricos não usam aspas "". Exemplo:
active_users = 5

Os números facilitam o controle dos dados numéricos. Como aqui, active_users armazena o número 5. Exemplo:
active_users = 5

Também podemos criar expressões com números. Aqui, podemos adicionar números com + 1. Exemplo:
number_of_applications = 5 + 1
print(number_of_applications) # Saída: 6

Usamos o sinal * para multiplicar números e o sinal “/” para dividir números. Transformaremos 0.5 em seu valor percentual multiplicando-o por 100. Exemplo:
percent = 0.5 * 100 
print (percent) # Saída: 50.0

Como sabemos que a variável score armazena um número?
score 40 + 4
# Porque não há aspas duplas em torno de 40 e 4

Multiplique a variável savings pela variável interest. Exemplo:
savings = 100
interest = 0.04
print(savings * interest) # Saída: 4.0

Divida sum_of_grades pelos students para obter a nota média de uma turma. Exemplo:
sum_of_grades = 460
students = 5
print(sum_of_grades / students) # Saída: 92.0

Subtraia discount do total e exiba o resultado do cálculo no console. Exemplo:
total = 100
discount = 20
print("Discounted price:")
print(total - discount) # Saída: Discounted price: 80

Como as expressões se tornam valores, podemos armazená-las em variáveis da mesma forma que os valores. Veja o exemplo aqui onde codificaremos label para exibir a expressão:
label "Posts: " + "13"
print(label) # Saída: Posts: 13

  


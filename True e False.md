# True e False

Em Python, `True` e `False` são os dois valores booleanos disponíveis, representando verdadeiro e falso, respectivamente. Esses valores são frequentemente usados em expressões lógicas e em estruturas de controle de fluxo, como condicionais e loops.

Por exemplo:

```python
verdadeiro = True
falso = False
```

## Exemplo 1: Verificando se um número é par:

```python
numero = 10
if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
```



## Exemplo 2: Verificando se uma lista está vazia:

```python
lista = []
if not lista:
    print("A lista está vazia")
else:
    print("A lista não está vazia")
```

## Exemplo 3: Verificando se uma condição é verdadeira:

```python
temperatura = 25
limite = 30
if temperatura < limite:
    print("A temperatura está abaixo do limite")
else:
    print("A temperatura está acima do limite")
```

Estes exemplos demonstram situações comuns em que `True` e `False` são usados para tomar decisões com base em condições booleanas. O primeiro exemplo verifica se um número é par, o segundo verifica se uma lista está vazia e o terceiro verifica se a temperatura está abaixo de um limite específico. Em cada caso, o código usa `True` ou `False` para determinar o fluxo de execução do programa.

#  Negando Valores

Às vezes, é útil negar o valor de uma expressão booleana, ou seja, inverter o seu resultado. Em Python, você pode fazer isso usando o operador `not`. Por exemplo:

```python
valor = True
negado = not valor  # negado agora é False
```

Neste exemplo, a variável `negado` terá o valor `False`, pois estamos negando o valor da variável `valor`, que é `True`.

## Exemplo 1: Verificando se um usuário não está logado:

```python
usuario_logado = False
if not usuario_logado:
    print("Por favor, faça login para continuar")
else:
    print("Bem-vindo!")
```

## Exemplo 2: Verificando se um item não está na lista:

```python
lista = [1, 2, 3, 4, 5]
item = 6
if item not in lista:
    print(f"O item {item} não está na lista")
else:
    print(f"O item {item} está na lista")
```

Nestes exemplos, o operador `not` é usado para negar o valor de uma variável ou de uma expressão. No primeiro exemplo, `not usuario_logado` verifica se o usuário não está logado. No segundo exemplo, `item not in lista` verifica se o item não está presente na lista. Em ambos os casos, a negação é usada para determinar o comportamento do programa com base na condição booleana negada.




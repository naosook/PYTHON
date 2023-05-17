#DESAFIO 01 - CÁLCULO DE MEDIA;

nota_01 = float(input("Qual o valor da 1º Nota?:"))
nota_02 = float(input("Qual o valor da 2º Nota?:"))
nota_03 = float(input("Qual o valor da 3º Nota?:"))
media = (nota_01 + nota_02 + nota_03) / 3
print("A Sua media final é:",round(media,2))

#DESAFIO 02 - CÁLCULO DE MEDIDA DE TEMPERATURA -> CELSIUS -> FAHRENHEIT;

grau_celsius = float(input("Cº Graus Celsius:"))
fahrenheit = (grau_celsius * 1.8) + 32
print("fahrenheit =", round(fahrenheit,2))

#DESAFIO 03 - CALCULAR O PERÍMETRO E A ÁREA DE UM RETÂNGULO;

base_b = int(input("Qual o valor da base(b)"))
altura_h = int(input("Qual o valor da base(h)"))
perimetro = 2*(base_b + altura_h)
print("Perimetro =", perimetro, "cm")
area_do_retangulo = (base_b * altura_h)
print("Area do Retangulo =", area_do_retangulo, "cm^2")


###
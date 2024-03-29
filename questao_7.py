#7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. 
#A fórmula de conversão é: 𝐶 = 5.0 ∗(𝐹−32.0)/9.0, sendo que 𝐹 a temperatura em 
#Fahrenheit e 𝐶 a temperatura em Celsius.

FAHRENHEIT = float( input("Digite a temperatura em graus Fahrenheit: ") )
CELSIUS =5.0 * ( FAHRENHEIT - 32.0) /9.0

print ( f" A conversão para graus Celsius é: {CELSIUS}")   
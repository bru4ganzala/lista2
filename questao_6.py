#6. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. 
#A fórmula de conversão é: 𝐹 = 𝐶 ∗ (9.0/5.0) + 32.0, sendo que 𝐹 a temperatura em 
#Fahrenheit e 𝐶 a temperatura em Celsius

CELSIUS = float( input("Digite a temperatura em graus Celsius: ") )
FAHRENHEIT = CELSIUS * (9.0/5.0)

print ( f" A conversão para graus Fahrenheit é: {FAHRENHEIT}")  

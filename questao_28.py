#28. A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso. 
#Sendo que da quantia total:
#a. O primeiro ganhador receberá 46%;
#b. O segundo receberá 32%;
#c. O terceiro receberá o restante;
#Calcule e imprima a quantia ganha por cada um dos ganhadores

PORCENTAGEMS = 46 + 32 
VALOR = 100 - PORCENTAGEMS 
PRRIMEIRO = 780.000 * 0.46
SEGUNDO = 780.000 * 0.32
TERCEIRO = 780.000 * VALOR 

print(f""" O primeiro ganhado recebera : {PRRIMEIRO} 
 O segundo ganhador recebera : { SEGUNDO}
 O terceiro ganhador recebera : {TERCEIRO}""")
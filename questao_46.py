#46. Sabendo que a média de aprovação é 7, e a formula para cálculo da média consiste em 
#a primeira avaliação com peso 1 e a segunda avaliação com peso 2, sendo divido por 3, 
#realize o cálculo de quanto deve ser a nota da segundo avaliação para que o resultado 
#seja a aprovação. Elabore a fórmula para o cálculo e a representação do algoritmo para o mesmo

N1 = float( input("Digite a nota 1 : ") )

media = 7

N2 = ((media * 3 )- N1 ) /2

print(f"A nota da segunda prova sera :{N2}")

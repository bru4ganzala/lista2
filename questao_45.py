#45. Calcule a média de um aluno na disciplina de ED. Para isso solicite o nome do aluno, a 
#nota da prova e a nota qualitativa. Sabe-se que a nota da prova tem peso 2 e a nota
#qualitativa peso 1. Mostre a média como resultado.


nome = input("Digite o nome do aluno :")
NP = float( input("Digite a nota de prova : ") )
NQ = float( input("Digite a nota qualitativa: ") )

media = (NQ + (NP * 2)) / 3

print ( f"A nota final da aluno(a) {nome} é:{media}")  

#15. Uma empresa de piscinas precisa saber qual o volume em que cada piscina terá em 
# M³, sendo que o usuário irá informar a largura, comprimento e profundidade.

LARGURA = float( input("Digite a largura da picina: ") )
COMPRIMENTO = float( input("Digite a comprimento da picina: ") )
PROFUNDIDADE = float( input("Digite a profundidade da picina: ") )

METROS = LARGURA * COMPRIMENTO * PROFUNDIDADE

print ( f" O volume que a picina tera em metros cubicos sera de : {METROS}")   



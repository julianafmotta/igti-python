# Jogo de Dados
# Escolho o valor entre 1 e 6
# Escolho quanto quero apostar Máximo 100 (valor que tenho no bolso) - ok
# Jogo 2 dados
# Se 1 dado igual ganho 2 vezes o valor apostado
# Se 2 dados derem iguais ganho 10 vezes o valor apostado
# Se não der nenhum dado igual perco meu dinheiro
#poderia fazer assim : questao = input("Qual número você aposta?"), mas o codigo fica mais bonito da forma abaixo
# faco um float na segunda pois o valor nao precisa ser inteiro
# gerar um numero aleatoio randrange não é uma funcao pronta, deve-se importar esta funcao  from random import e insere o nome da funcao
from random import randrange
bolso = 100
numero_apostado = int(input("Qual número você aposta?"))
valor_aposta = float(input("Qual o valor da aposta?"))
if valor_aposta>bolso:
  print("Voê não tem esse dinnheiro")
else:  
  bolso = bolso - valor_aposta
  dado1 = randrange(1,6)
  dado2 = randrange(1,6)
  mensagem_ganho = "Você ganhou {} e agora está com {}"
  print("Sorteados os dodos {} e {}".format(dado1,dado2))
  resultado = 0 
  if (dado1==numero_apostado)and(dado2==numero_apostado):
    resultado = valor_aposta * 10
    bolso = resultado + bolso 
    print("Você ganhou {} e agora está com {}".format(resultado,bolso))
  elif (dado1==numero_apostado)or(dado2==numero_apostado):
    resultado = valor_aposta * 2  
    bolso = resultado + bolso
    print("Você ganhou {} e agora está com {}".format(resultado,bolso))
  else:
    print("Você errou. Agora tem no bolso {}".format(bolso))


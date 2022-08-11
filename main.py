"""
Alunos: Samir Avelino Carvalho, Vitor de Paula Batista

  Algoritmo genético para encontrar o x para o qual a função x^2 - 3x + 4 assume o valor máximo
  Assumir que x [-10, +10]
  Codificar X como vetor binário
  Criar uma população inicial com 4  indivíduos
  Aplicar Mutação com taxa de 1%
  Aplicar Crossover com taxa de 70%
  Usar seleção por torneio.
  Usar 5  gerações

"""


import numpy as np
import random

# Gera uma população de um determinado tamanho com individuos que possuem um # número expecífico de bits
def gerarIndividuosAleatorios():
    populacao = []
    for i in range(4):
        populacao.append(np.random.choice(range(-10, 10), replace=False)) 
    return populacao

 # calculando o número de bits convertento no formato binário 
def binarioIndividuos(individuos):
  indBin = []
  for i in individuos:
    indBin.append(convertBinario(i))
  return indBin

  #converte para binario
def convertBinario(decimal):
  b = f'{(decimal+10):05b}'
  return stringParaVetor(b)

def stringParaVetor(binario):
  bi = []
  for i in range(5):
    bi.append(int(binario[i]))
  return bi

# Realiza a mutação de um indiviuo conforme uma dada probabilidade (taxa de mutação)
def mutar(individuos):
  for i in individuos:
    #taxa de mutação 0,010
    if np.random.uniform(0, 1) < 0.011:
      i = mutacao(i)
  return individuos

def mutacao(ind1):
  corte = random.randint(0, 5)
  if ind1[corte] == 1 : ind1[corte]=0
  else: ind1[corte] = 1
  return ind1

#realiza a seleção por torneio
def torneio(individuos):
  novosInd = []
  propIndividuos = gerarProporcao(individuos)
  while len(novosInd) != 4:
    i1 = selecionarIndividuo(individuos, propIndividuos)
    i2 = selecionarIndividuo(individuos, propIndividuos)
    if funcao(i1) < funcao(i2):
      novosInd.append(i1)
    else:
      novosInd.append(i2)
  return novosInd

def selecionarIndividuo(individuos, propIndividuos):
  roleta = np.random.uniform(0, 1)
  intervalos = vetorIntervalos(propIndividuos)
  for i in range(len(individuos)):
    if roleta > intervalos[i] and roleta < intervalos[i+1]:
      return individuos[i]

def gerarProporcao(individuos):
  apitTotal = apTotal(individuos)
  apIndividuos = apetidaoIndividuos(individuos)
  propIndividuos = []
  for a in apIndividuos:
    propIndividuos.append(a/apitTotal)
  return propIndividuos

def apTotal(individuos):
  apInd = apetidaoIndividuos(individuos)
  apTotal = 0
  for a in apInd:
    apTotal = apTotal + a
  return apTotal

# Aplica o crossover de acordo com uma dada probabilidade (taxa de crossover) 
def crossover(i1, i2):
  individuo1 = convertBinario(i1)
  individuo2 = convertBinario(i1)
  posicaoCorte = random.randint(0, 5)
  filho = []
  for i in range(posicaoCorte):
    filho.append(individuo1[i])
  for i in range(5-posicaoCorte):
    filho.append(individuo2[i])
  return filho

def cruzamento(individuos):
  counti = 0
  novosIndividuos = []
  for i in individuos:
    countj = 0
    for j in individuos:
      taxa = np.random.uniform(0, 1)
      #aplicando a uma taxa de 0.70
      if counti != countj and taxa < 0.71:
        novosIndividuos.append(crossover(i, j))
      countj = countj+1
    counti = counti+1
  return novosIndividuos 
  
def apetidaoIndividuos(individuos):
  aptidaoPop = []
  for x in individuos:
    aptidaoPop.append(funcao(x))
  return aptidaoPop

# Calcula a função utilizada para avlaiar as soluções produzidas # Função é dada por x^2 - 3x + 4
def funcao(x):
  return x*x - 3*x + 4


def decimalIndividuos(individuos):
  decimal = []
  for i in individuos:
    decimal.append(converterParaDecimal(i))
  return decimal


def converterParaDecimal(binario):
  temp = vetorParaString(binario)
  return (int(temp,2)-10)

def vetorParaString(binario):
  dec = ""
  for i in binario:
    dec = dec + str(i)
  return dec


def vetorIntervalos(propIndividuos):
  intervalosIndividuos = []
  intervalosIndividuos.append(0)
  for i in range(len(propIndividuos)):
    intervalosIndividuos.append(intervalosIndividuos[i]+propIndividuos[i])
  return intervalosIndividuos

  
individuosDec = gerarIndividuosAleatorios()
print("Individuos Gerados: \n",individuosDec, "\n")

individuosBin = binarioIndividuos(individuosDec)
print("Valor Binario dos Individuos:\n ",individuosBin, "\n")

apIndividuos = apetidaoIndividuos(individuosDec)
print("Apetidão dos Individuos:\n ",apIndividuos, "\n")

propIndividuos = gerarProporcao(individuosDec)
print("Proporção Individuos: \n",propIndividuos, "\n")

novosIndividuos = cruzamento(individuosDec)
print("Novos Individuos: \n", novosIndividuos, "\n")

mutacaoIndividuos = mutar(novosIndividuos)
print("Valor Decimal dos Novos Individuos:\n",decimalIndividuos(novosIndividuos), "\n")

print("\nApetidão dos Novos Individuos: \n",apetidaoIndividuos(decimalIndividuos(novosIndividuos)), "\n")

selecionarIndividuos = torneio(decimalIndividuos(novosIndividuos))
print("Individuos Selecionados: \n",selecionarIndividuos, "\n")
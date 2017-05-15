# coding: utf-8
from time import sleep
from random import randrange
# IMPLEMENTAR DICAS ALEATORIAS + CONTADOR DE DICAS
# IMPLEMENTAR DESISTENCIA


def minusc(str):
	return str.lower()
	


def chavear():
	file = open('chaves.txt','r')
	lista = file.read().split()
	for e in range(0,len(lista),2):
		chaves[lista[e]] = lista[e+1]
	

def ensinar(nomedoconjunto):
	file = open('%s.txt'%nomedoconjunto,'a')
	if nomedoconjunto not in chaves:
		chave = open('chaves.txt','a')
		chave.write('%d %s '%(len(chaves),nomedoconjunto))

	while True:
		palavra = raw_input('digite um membro-> ')
		if palavra == '-': break
		file.write('%s '%palavra)
	file.close()
	chave.close()
	chavear()



def jogar(n):
	parametro = chaves[n]
	file = open('%s.txt'%parametro,'r')
	lista =  map(minusc,file.read().split())
	print lista[0]
	lista1 = []
	while True:
		a = raw_input()
		if a == '-%s'%parametro:
			print 'voce venceu!'
			print ''
			print ''
			print ''
			break
		elif a == '-': break
		if a in lista and a not in lista1:
			print 'pode levar'
			lista1.append(a)
		elif a in lista:
			print 'já levaram'
		else:
			print 'não pode levar'
	
	
plot_inic = 'DEUS E TOP'
chaves = {}
chavear()
for e in plot_inic:
	print e
	sleep(0.1)
while True:
	print 'ensinar jogar sair chaves'
	print ''
	print 'selecione uma opção'
	a = raw_input()
	if a == 'chaves':
		for e in chaves:
			print chaves[e],
		print ''
		print ''
	elif a == 'sair': break
	elif a == 'ensinar':
		r = raw_input('oque voce vai ensinar? -> ')
		ensinar(r)

	elif a == 'jogar':
		b = randrange(0,len(chaves),1)
		jogar(str(b))






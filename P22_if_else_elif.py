#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ coding: utf-8 _*_

#Al siguiente c�digo a��dele un par de rangos de edad. Uno de 18 a�os hasta 45 y otro de m�s de 
#100 a�os hasta 120.

#edad = int(input('�Cu�l es tu edad?\n'))
#if edad <= 0:
#	print('Nadie puede tener esa edad.')
#elif edad <= 1 and edad < 18:
#	print('Eres menor de edad.')
#elif edad <= 100:
#	print('Eres mayor de edad.')
#else:
#	print('Edad no v�lida.')

edad = int(input("�Cual es tu edad?\n"))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad < 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
	print('Eres un adulto joven')
elif edad >45 and edad <= 100:
	print('Eres un adulto viejo.')
elif edad >100 and edad <= 120:
	print("Wow, es usted muy viejo")
else:
	print('Edad no v�lida.')
#Elimina de la siguiente lista los elementos 'azul' y 'blanco' utilizando el m�todo pop(). 
#Adem�s, tendr�s que guardar esos dos colores en una nueva lista.

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

valor1 = colores.pop(7) #eliminamos de la lista el color azul y lo guardamos en una variable
valor2 = colores.pop(-4) #eliminamos de la lista el color blanco y lo guardamos en una variable

print(colores) #comprobamos que se haya eliminado

lista2 =[valor1 , valor2] #creamos la nueva lista con estos dos valores
print(lista2) #imprimimos la nueva lista
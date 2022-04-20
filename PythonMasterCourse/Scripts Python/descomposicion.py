'''**3) [Avanzado] Crea un script llamado descomposicion.py que realice las siguientes tareas:**
* Debe tomar 1 argumento que será un número entero positivo.
* En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.

** El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número:**

```
> 3647
```
** El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo: **

```
> 0007
  0040
  0600
  3000
```
*Pista: Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa*'''

import sys
if len(sys.argv) == 2:
  numero = int(sys.argv[1])
  cadena =str(numero)
  for i in range(len(cadena)):
    print("{:04d}".format(int(cadena[len(cadena)-1-i])* 10 ** i))  
    
else:
  print("Datos incorrectos")
#! /usr/bin/python
#-------------------------------------------------------------------------------
# Asignatura: Herramientas Informaticas de Alto Nivel (2013 / 2014)
# Autores:
#   - Bentorey Hernandez
#   - Manuel de Leon
#   - Ismael de la Viuda
# Observaciones:
#   Uso:
#     $./modulo_equal.py
#     $./modulo_equal.py <expr1> <expr2> <min_value> <max_value> <numero_test>
#   Define la funcion equal, que tratara de evaluar si dos expresiones matemati-
#  cas son equivalentes devolviendo el porcentaje de errores al evaluarlas y
#  compararlas.
#   Ademas, permite realizar una ejecucion de ejemplo o evaluar en linea de
#  comandos dos expresiones distintas
#-------------------------------------------------------------------------------
# Importamos sys para operar sobre los parametros pasados en linea de comandos
# y random para la generacion de numeros aleatorios
# math y numpy son necesarias para la evaluacion de expresiones matematicas
import sys
import random
from math import *
from numpy import *

#-------------------------------------------------------------------------------
# Funcion: equal
# Parametros:
#   - expr1: Primera expresion a evaluar (str)
#   - expr2: Segunda expresion a evaluar (str)
#   - A: Limite inferior de los numeros aleatorios generados (float)
#   - B: Limite superior de los numeros aleatorios generados (float)
#   - n: Numero de ejecuciones (int)
# Ejecucion: evalua n veces dos expresiones devolviendo el numero de fallos que
#  se producen a la hora de compararlas
#-------------------------------------------------------------------------------
def equal(expr1, expr2, A, B, n):
  total = n
  nFallos = 0.0
  for i in range(0,n):
      a = random.uniform(A,B)
      b = random.uniform(A,B)
      try:
        if (eval(expr1) != eval(expr2)):
            nFallos += 1
      except:
        total -= 1
  if (total == 0.0):    # En caso de que se hayan producido fallos en todas las
      return 100.0      # expresiones, devolvemos 100 % de error
  return ((nFallos / float(total)) * 100.0)

#-------------------------------------------------------------------------------
# Siguiendo el ejemplo de ejecucion del guion de la practica
# /practicas/src$ ./modulo_equal.py \(a*b\)**3 a**3*b**3 -100 100 10000
# procedemos a reconocer los parametros actuales, en caso de que haya
# un fallo, abortaremos la ejecucion

# Bloque de comprobaciones
if __name__ == '__main__':
  errorEntrada = False       # Contralamos que los valores pasados por linea de
  if (len(sys.argv) != 6):   # comandos esten y que sean correctos
    errorEntrada = True
  else:
    try:
      float(sys.argv[3])
      float(sys.argv[4])
      int(sys.argv[5])
    except: # En caso de que se produzcan errores a la hora de reconocer
            # los parametros numericos
      errorEntrada = True

  if (errorEntrada):
    print "La forma de uso es ./modulo_equal.py expr1 expr2 min_value max_value numero_test"
    print "Se usan los valores por defecto:"
    print "./modulo_equal.py  expr1       expr2       min_value   max_value    numero_test   fallos"
    print "./modulo_equal.py  (a*b)**3 (a**3)*(b**3)   -100.0       100.0         500        ", equal("(a*b)**3", "(a**3)*(b**3)", -100.0, 100.0, 500)
    print "./modulo_equal.py  (a/b)      1/(b/a)       -100.0       100.0         500        ", equal("(a/b)", "1/(b/a)", -100.0, 100.0, 500)
  else:
    print sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
    try:
        porcentajeFallos = equal(sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]))
    except:
        print "Se ha producido un error durante la ejecucion"
        exit()
    print "Porcentaje de Fallos", porcentajeFallos
#-------------------------------------------------------------------------------
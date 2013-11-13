#! /usr/bin/python
#-------------------------------------------------------------------------------
# Asignatura: Herramientas Informaticas de Alto Nivel (2013 / 2014)
# Autores:
#   - Bentorey Hernandez
#   - Manuel de Leon
#   - Ismael de la Viuda
# Observaciones:
#   Uso:
#     $./identidades.py
#     $./identidades.py <lim inf rango> <lim sup rango> <iteraciones>
#   Genera una lista de funciones a evaluar y realiza las llamadas pertinentes
#  a equal (disponible en el modulo modulo_equal.
#   Muestra una tabla con los resultados obtenidos
#-------------------------------------------------------------------------------
import sys
from modulo_equal import equal
from math import *
 
# Cada una de las expresiones
a1 = "(a*b)**3" 
a2 = "(a**3)*(b**3)"
b1 = "a/b"
b2 = "1/(b/a)"
c1 = "exp(a+b)"
c2 = "(exp(a))*(exp(b))"
d1 = "log(a**b)"
d2 = "b*log(a)"
e1 = "a-b"
e2 = "-(b-a)"
f1 = "(a*b)**4"
f2 = "(a**4)*(b**4)"
g1 = "(a+b)**2"
g2 = "(a**2)+2*a*b+(b**2)"
h1 = "(a+b)*(a-b)"
h2 = "(a**2)-(b**2)"
i1 = "log (a*b)"
i2 = "log(a)+log(b)"
j1 = "a*b"
j2 = "exp(log(a)+log(b))"
k1 = "1/((1/a)+(1/b))"
k2 = "a*b/(a+b)"
l1 = "a*(((sin(b))**2) + ((cos(b))**2))"
l2 = "a"
m1 = "sinh(a+b)"
m2 = "((exp(a)*exp(b))-(exp(-a)*exp(-b)))/2"
n1 = "tan(a+b)"
n2 = "(sin(a+b))/(cos(a+b))"
o1 = "sin(a+b)"
o2 = "(sin(a)*cos(b))+(sin(b)*cos(a))"

# Lista con las identidades a evaluar
identidades = [(a1, a2), (b1, b2), (c1, c2), (d1, d2), (e1, e2), (f1 ,f2), (g1, g2), (h1, h2), (i1, i2), (j1, j2), (k1, k2), (l1, l2), (m1, m2), (n1, n2), (o1, o2)]

if __name__ == '__main__':
    falloparametros = False 
    if len(sys.argv) == 4: # Intentamos recuperar los parametros por linea de
        try:               # comandos
            A = float (sys.argv[1])
            B = float (sys.argv[2])
            n = int (sys.argv[3])
        except: 
            falloparametros = True    
    else:
        falloparametros = True
    
    if falloparametros: #   En caso de que los parametros no sean validos o
        A = -100.0      # que no se hayan introducido, evaluamos con los
        B = 100.0       # valores por defecto
        n = 500
        print "Se produjo un error al recuperar los parametros por linea de comandos"
        print "Se usan los valores por defecto"
        print "\tA = -100.0"
        print "\tB = 100.0"
        print "\tn = 500"
        
    # Nos preparamos para mostrar la tabla de resultados
    # Obtenemos la maxima longitud de las expresiones
    maxLen = 0
    for i in identidades:
        if (len(i[0]) > maxLen):
            maxLen = len(i[0])
        if (len(i[1]) > maxLen):
            maxLen = len(i[1])
   
    # Cadena con el formato para mostrar por pantalla
    forma = "{0:^" + str(maxLen) + "}"
    
    print forma.format("expr1"), forma.format("expr2"), " min_value     max_value    numero_test  fallos"
    
    for i in identidades:
        expr1 = forma.format(i[0])
        expr2 = forma.format(i[1])
        val = equal(i[0], i[1], A, B, n)
        print expr1, expr2, "  "+ str(A)+"\t    ", str(B)+"\t  ", str(n)+"\t     ", "{0:.2f}".format(val)
#-------------------------------------------------------------------------------
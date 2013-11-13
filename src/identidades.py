#! /usr/bin/python
import sys
from modulo_equal import equal
from math import *
 
 
def formatStr(palabra, maxLen):
    cond = True
    pal = palabra
    while len(pal) < maxLen:
        if cond:
            pal = " " + pal
        else:
            pal = pal + " "
        cond = not cond
    return pal
 
 
 
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

identidades = [(a1, a2), (b1, b2), (c1, c2), (d1, d2), (e1, e2), (f1 ,f2), (g1, g2), (h1, h2), (i1, i2), (j1, j2), (k1, k2), (l1, l2), (m1, m2), (n1, n2), (o1, o2)]


if __name__ == '__main__':
    falloparametros = False 
    if len(sys.argv) == 4:
        try:
            A = float (sys.argv[1])
            B = float (sys.argv[2])
            n = int (sys.argv[3])
        except: 
            falloparametros = True    
    else:
        falloparametros = True
    
    if falloparametros:
        A = -100.0
        B = 100.0
        n = 500
        print "Se produjo un error al recuperar los parametros por linea de comandos"
        print "Se usan los valores por defecto"
        print "\tA = -100.0"
        print "\tB = 100.0"
        print "\tn = 500"
        
        
    # Nos preparamos para mostrar la tabla de resultados
    
    maxLen = 0
    for i in identidades:
        print i,len(i[0]),len(i[1])
        if (len(i[0]) > maxLen):
            maxLen = len(i[0])
        if (len(i[1]) > maxLen):
            maxLen = len(i[1])
    print "La maxima longitud es:", maxLen
    
    #tabla = []
    #for i in identidades:
    #    expr1 = formatStr(i[0], maxLen)
    #    expr2 = formatStr(i[1], maxLen)
    #    tabla.append([expr1, expr2])
    
    
    
    print formatStr("expr1",maxLen), formatStr("expr2", maxLen), " min_value     max_value    numero_test  fallos"
    
    forma = "{0:^" + str(maxLen) + "}"
    for i in identidades:
        #expr1 = "{0:^" + str(maxLen) + (i[0], maxLen)
        #expr2 = formatStr(i[1], maxLen)
        expr1 = forma.format(i[0])
        expr2 = forma.format(i[1])
        val = equal(i[0], i[1], A, B, n)
        print expr1, expr2, "  "+ str(A)+"\t    ", str(B)+"\t  ", str(n)+"\t     ", "{0:.2f}".format(val)
    
    
    
    
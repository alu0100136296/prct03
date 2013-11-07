#! /usr/bin/python

from modulo_equal import *
from numpy import *
from math import *
 
a1 = "(a*b)**3" 
a2 = "(a**3)*(b**3)"
b1 = "a/b"
b2 = "1/(a/b)"
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
h1 = "(a+b)(a-b)"
h2 = "(a**2)-(b**2)"
i1 = "log (a*b)"
i2 = "log(a)+log(b)"
j1 = "a*b"
j2 = "exp(ln(a)+ln(b))"
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
print equal (e1, e2, 2, 5, 100)
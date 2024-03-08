import re

from verify.judge import Judge
import sympy

judge = Judge("", "")
out = ("-84*exp((12*x**2-12*x**8-12*x**8*exp(x)**2-24*x**8*exp(x)+3*x**14+18*x**14*exp(x)**2+12*x**14*exp("
       "x)**3+3*x**14*exp(x)**4+12*x**14*exp(x)))-x**7")
print(judge.is_legal(out))

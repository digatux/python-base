#!/usr/bin/env python

""" Imprimi a tabuada de 1 a 10

exemplo
Tabuada do 1
1
2
3
---------------
Tabuada do 2
2
4
6
-------------
"""
__version__ = "0.1.0"
__autor__ = "Edgar Silva"

numeros = range(1,11)

for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print()
    print("#" * 18)

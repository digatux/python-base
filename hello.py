#!/usr/bin/env python3
"""
Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente

Como Usar:

Tenha a variavel Lang devidamente configura ex:

    export LANG=pt_BR

Execucao:

    python3 hello.p
    ou
    ./hello.py 

obs.: para que ./hello.py funcione é necessario deixa-lo como executavel no linux  
$ chmod +x ./hello.py


"""
__version__ = "0.0.1"
__author__ = "Edgar Silva"
__license__ = "Unlicense"


import os


current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World"

if current_language ==  "pt_BR":
    msg = "Olá, Mundo!"
if current_language == "it_IT":
    msg = "Ciao, Mondo"


print(msg)

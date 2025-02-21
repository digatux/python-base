#!/usr/bin/env python3
"""
Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente

Como Usar:

Tenha a variavel Lang devidamente configura ex:

    export LANG=pt_BR

    ou informe atraves do CLI arguments `--lang`
    ou o ususario tera aque digitar

Execucao:

    python3 hello.p
    ou
    ./hello.py 

obs.: para que ./hello.py funcione é necessario deixa-lo como executavel no linux  
$ chmod +x ./hello.py


"""
__version__ = "0.1.3"
__author__ = "Edgar Silva"
__license__ = "Unlicense"


import os
import sys



arguments = {
        "lang": None,
        "count": 1,
}


for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit
    arguments[key] = value


current_language = arguments["lang"]
if current_language is None:
    # TODO; Usar Repeticao
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language: ")

current_language = current_language[:5]

msg = {
    "en_US": "Hello World!",
    "pt_BR": "Olá Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola, MUndo!",
    "fr_FR": "Bonjour, Monde!",
}

"""
msg = "Hello, World"

if current_language ==  "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"
"""

print(msg[current_language] * int(arguments["count"]))

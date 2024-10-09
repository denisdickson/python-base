#!/usr/bin/env python3
"""
hello world multi linguas

dependendo da lingua configurada no ambiente o programa exibe a msg 
correspondente
manter código até coluna 0-79

Como usar:

Tenha a variavel LANG devidamente configurada ex:
    export LANG=pt_br

Execução:
    python3 hello.py
    ou
    ./hello.py
"""

#which python3 --> /usr/bin/python3 boa prática especificar shebang
#print('denis'.upper())
#print( 26+9)
#print("comentários foram feitos")
#print("shebang foi adicionado também")

__version__="0.0.1"
__author__="Denis" #Dunder __word__ [double under]
__license__="Unlicense"
import os

#if __name__ == "__main__": #Define bloco principal 
current_language= os.getenv("LANG", "en_US")[:5]

msg="Hello, World!"

if current_language == "pt_BR.UTF-8":
    msg = "Olá,Mundo"
elif current_language == "it_IT":
    msg = "Ciao,Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde"    
print(msg)

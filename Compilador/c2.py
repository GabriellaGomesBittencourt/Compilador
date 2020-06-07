import re

pascal_keys=""
pascal_code=""

with open("pascal-keys.txt","r") as pkeys:
    pascal_keys = pkeys.read().split()

with open("p1.pas","r") as pkeys:
    pascal_code = pkeys.read().lower().replace("["," [ ").replace("]"," ] ").replace('(',' ( ').replace(')',' ) ').replace('\n','').replace(';',' ; ').split(' ')

lexemas=[]
integerPattern =  r"^[-+]?[0-9]+$"
floatPattern =  r"^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$" 
operationPattern = r"[0-9A-Za-a]*( ){0,}([+-/*]( ){0,}[0-9A-Za-a]*( ){0,})*"

for token in pascal_code:
    if token in pascal_keys:
       lexemas.append([token,"key word"])
    elif re.match(integerPattern, token):
       lexemas.append([token,"integer"])
    elif re.match(floatPattern, token):
       lexemas.append([token,"float"]) 
    elif (token == '('):
       lexemas.append([token,"open parentese"]) 
    elif (token == ')'):
       lexemas.append([token,"close parentese"]) 
    elif (token == '['):
       lexemas.append([token,"open brackets"]) 
    elif (token == ']'):
       lexemas.append([token,"close brackets"])
    elif (token == ';'):
        lexemas.append([token,"pontuation"])    
    elif (token == '+' or token == '.' or token == '-' or token == '*' or token == '^' or token == '=' or token == ':=' ):
       lexemas.append([token,"operation"]) 
    elif ( token == ''):
        lexemas.append([token,"espace"])
   
    else:
       lexemas.append([token,"unknow"])

#print(pascal_keys)
#print(pascal_code)
print(lexemas)

with open("tokens.txt","w") as lexemas_file:
    lexemas_file.write(str(lexemas))

# 1. ler arquivo
# 2. quebrar em tokens
# 3. usar regexp para verificar o tipo de token

# palavras reservadas - keywords
# float
# int
# variáveis -> regexp
# operações (+, -, *, ^, =, :=)

# Lex - Parser >>> WEB Scraping

# TODO: Terminar...
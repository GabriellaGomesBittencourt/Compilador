message="E ai galera do Corinthians!!"

for palavra in message.split():
    print(palavra)

for cara in message:
    print(cara)

coisas="C !"
operacoes = "+-.^*="

# Lexico - Scanner

for cara in message:
    if cara in coisas:
        print([cara, type(cara), len(cara)])


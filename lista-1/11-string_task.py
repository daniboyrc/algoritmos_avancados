from sys import stdout

string = raw_input().lower()

lista = "aoyeui"
for i in xrange(len(lista)):
  if lista[i] in string:
    string = string.replace(lista[i], "")
    
for i in string:
  stdout.write('.'+i)

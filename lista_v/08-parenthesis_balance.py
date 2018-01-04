# https://www.urionlinejudge.com.br/judge/en/problems/view/1068

try:
    while True:
        expressao = raw_input()
        lista = []
        for i in expressao:
            if i == "(":
                lista.append(i)
            elif i == ")" and len(lista) == 0:
                lista = [1]
                break
            elif i == ")":
                lista.pop()
        if len(lista) == 0:
            print 'correct'
        else:
            print 'incorrect'
except:
    pass 

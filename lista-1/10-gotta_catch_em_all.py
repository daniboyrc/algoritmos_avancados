string = raw_input()

a = min([string.count('B'), string.count('l'), string.count('b'), string.count('s'), string.count('r')])
b = min([string.count('a'), string.count('u')]) // 2

print min([a, b])

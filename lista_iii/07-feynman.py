while True:
    square = int(raw_input())
    if square == 0:
        break
    soma = 0
    for i in range(square + 1):
        soma += i ** 2

    print soma

def n_linhas(n):
    for x in range(1, n + 1):
        print(end ='\n')
        for y in range(x):
            print(x, end='')


n = int(input("Quantas linhas? "))

n_linhas(n)

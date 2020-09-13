def showNumbers(limit):

    for i in range(1 ,limit + 1):
        if i % 2 == 0:
            print(f'{i} EVEN')
        else:
            print(f'{i} ODD')


showNumbers(10)

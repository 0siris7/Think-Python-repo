def magic_square(n):
    magicSquare = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0) #List l is appended with n 0's

        magicSquare.append(l) #Append list to the magic square list

    i = n // 2
    j = n - 1

    num = n * n
    count = 1
    while count <= num:
        if i == -1 and j == n:
            j = n - 2
            i = 0

        else:
            if j == n :
                 j = 0 #Col val exceed
            if i < 0:
                i = n - 1 #Row is -1 counter val

        if magicSquare[i][j] != 0:
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[i][j] = count
            count += 1

        i -= 1
        j += 1
    for i in range(n):
        print(*magicSquare[i])

magic_square(3)

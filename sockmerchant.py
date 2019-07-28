
def sockMerchant(n, ar):
    count = 0
    for i in range(n):


        for j in range(i + 1, n):
            """print("------")
            print(f"{ar[i]}\n {ar[j]}")
            print("-------")"""
            if ar[i] is ar[j]:
                count = count + 1


    return count



if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))
    #print(ar)
    result = sockMerchant(n, ar)

    print(result)

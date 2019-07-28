def print_formatted(number):
    k = ''
    for i in range(1, number + 1):
        k += f"{i}\t{oct(i)}\t{hex(i)}\t{bin(i)}\n"
    print(k)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

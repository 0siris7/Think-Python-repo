string = list(input())


def palindrome(string):
    i = 0
    j = len(string) - 1

    while i <= j:
        if string[i] == string[j] == '.':
            string[i] = 'a'
            string[j] = 'a'

        elif string[i] != string[j]:
            if string[i] == '.':
                string[i] = string[j]

            elif string[j] == '.':
                string[j] = string[i]


            else:
                return -1

        i += 1
        j -= 1

    return "".join(string)


final = palindrome(string)
print(final)
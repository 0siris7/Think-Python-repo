def recurer(i,k,count):
    for k in range(i + 1,len(s) + 1):
        if s[i : k] in s:
            #print(s[i : k])
            count += 1

    return count 



def minion_game(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    count1 = 0
    count2 = 0

    for i in range(len(s)):
        if s[i] not in vowels:
            for k in range(i + 1,len(s) + 1):
                if s[i : k] in s:
                    #print(s[i : k])
                    count1 += 1
        else:
            for k in range(i + 1,len(s) + 1):
                if s[i : k] in s:
                    #print(s[i : k])
                    count2 += 1


    return count1, count2


total = minion_game('BANANA')
print(*total)

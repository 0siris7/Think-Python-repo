bin_num = str("{0:b}".format(int(input()))) #Convert decimal to binarey
#print(bin_num)
temp = bin_num.split('0') #Split string at 0's
print(len(max(temp))) #find max length string and print len

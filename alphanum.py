import re
mix = input()
array = re.findall(r'[0-9]+', mix)
num_arr = [int(x) for x in array]  
print(max(num_arr))
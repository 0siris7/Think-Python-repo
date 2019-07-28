prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letters in prefixes:
    if letters is 'O' or letters is 'Q':
        print(letters + 'uack')
    else:
        print(letters + suffix)

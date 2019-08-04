filename = 'poll.txt'

with open(filename, 'w') as fob:
    while True:
        poll = input("So, why ya like programming?")
        if poll == 'q' or poll == 'quit':
            break

        else:
            fob.write(poll + '\n') 

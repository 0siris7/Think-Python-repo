filename = 'sherlock.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()

except FileNotFoundError:
    print(f"File {filename} does not exist")

else:
    #count number of words
    words = contents.split()
    num_words = len(words)
    print(f"File {filename} has {num_words} words")

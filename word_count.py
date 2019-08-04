def count_words(filename):
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


filenames = ['sherlock.txt', 'emma.txt', 'mobydick.txt']
for filename in filenames:
    count_words(filename)

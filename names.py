from name_function import get_formatted_name

print("Enter 'q' to quit at any time")
while True:
    first = input("\nEnter your first name: ")
    if first == 'q':
        break
    last = input("\nEnter your last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\nneatly formatted name: {formatted_name}.")

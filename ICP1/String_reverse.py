from random import randint


# function to delete given number of characters from the string and to reverse the remaining string
def reverse_string(str):
    new_string= ""
    for x in range(0, int(num)):
        pos = randint(0, len(str) - 1)
        new_string += str[pos]
        str = str[:pos] + str[pos + 1:]
    print('Randomly deleted characters are:', new_string)
    print('String after deleting the characters:', str)
    print('Reversed string:', str[::-1])


# user input
input_string = input("Enter the string:")
num = input("Enter number of Characters to be deleted: ")

# Calling the function
reverse_string(input_string)

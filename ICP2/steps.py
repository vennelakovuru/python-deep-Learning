# user input to enter a number
number = int(input("Enter the number to reduce zero:"))
sum_of_steps = 0
num = number

# while loop dividing the number by 2 when its even and subtracting 1 when its odd to reduce it to zero
while num != 0:
    # check if num is odd or even
    if num % 2 == 0:
        # num is even
        sum_of_steps = sum_of_steps + 1
        print(f"step {sum_of_steps}: {num}  is even;")
        num = num/2
        print(f"divided by 2 and obtained {num}")
    else:
        # num is odd
        sum_of_steps = sum_of_steps + 1
        print(f"step {sum_of_steps}: {num} is odd;")
        num = num-1
        print(f"subtracted 1 and obtained {num}")

# print the number of steps obtained

print(f"Number of steps to reduce {number} to Zero: {sum_of_steps}")


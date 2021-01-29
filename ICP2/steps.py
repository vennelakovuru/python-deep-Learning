number = int(input("Enter the number to reduce zero:"))
sum_of_steps = 0

num = number

while num != 0:
    if num % 2 == 0:
        sum_of_steps = sum_of_steps + 1
        print(f"step {sum_of_steps}: {num}  is even;")
        num = num/2
        print(f"divided by 2 and obtained {num}")
    else:
        sum_of_steps = sum_of_steps + 1
        print(f"step {sum_of_steps}: {num} is odd;")
        num = num-1
        print(f"subtracted 1 and obtained {num}")

print(f"number of steps to reduce {number} to Zero: {sum_of_steps}")


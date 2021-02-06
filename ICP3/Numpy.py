import numpy as np

# using numpy random to create array of size 20 having only float in the range 1-20.
random_array = np.random.uniform(low=1, high=20, size=20)
print("random array in the range of 1 to 20::")
print("--------------------------------------")
print(random_array)

# using numpy reshape method to convert the random array to 4 by 5
reshape_array = random_array.reshape(4, 5)
print("Reshaping array to 4 by 5::")
print("---------------------------")
print(reshape_array)

# using numpy where we specify a condition and return the array based on it
maxZero_array = np.where(reshape_array == np.max(reshape_array, axis=1).reshape(-1, 1), 0, reshape_array)
print("Replacing max element in each array to 0:::")
print("===========================================")
print(maxZero_array)

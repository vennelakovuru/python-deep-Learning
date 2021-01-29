# reading file wcInput.txt
inputFile = open("wcInput.txt", 'r')
wordCount = dict()

# reading line
line = inputFile.readline()
while line != "":
    # returns a copy of the string by removing both the leading and the trailing characters.
    line = line.strip()
    # splitting each line separated by space and treating as individual words
    for x in line.split(" "):

        # If word found in dictionary wordCount its value increases by 1
        # else new word is added to the dictionary
        if x in wordCount.keys():
            wordCount[x] = wordCount[x] + 1
        else:
            wordCount[x] = 1
    line = inputFile.readline()

# Writing the word and its count to the output file
with open('wcOutput.txt', 'w') as file:
    for key, value in wordCount.items():
        file.write('{0}: {1}\n'.format(key, value))
print("Output is written to the file wcOutput.txt")
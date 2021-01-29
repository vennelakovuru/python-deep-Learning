infile = open("wcInput.txt", 'r')
wordCount = dict()
line = infile.readline()
while line != "":
    line = line.strip()
    for x in line.split(" "):
        # print(wordDict)
        # print(x)
        if x in wordCount.keys():
            wordCount[x] = wordCount[x] + 1
        else:
            wordCount[x] = 1
    line = infile.readline()

with open('wcOutput.txt', 'w') as file:
    for key, value in wordCount.items():
        file.write('{0}: {1}\n'.format(key, value))

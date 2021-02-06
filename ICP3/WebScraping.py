import requests
from bs4 import BeautifulSoup

html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
soup = BeautifulSoup(html.content, "html.parser")

# getting title of the page
print("Title of the page::", soup.title.string)

# Finding all the links with the tag a from html page
alinks= soup.find_all('a')

# initializing the file with write permission
file_write = open("links.txt", "w")

# looping over the alinks to get the href values and writing it to the file
for link in alinks:
    links = link.get('href')
    if links is not None:
        file_write.write(links)
        file_write.write("\n")
print("Links are saved in the file links.txt")



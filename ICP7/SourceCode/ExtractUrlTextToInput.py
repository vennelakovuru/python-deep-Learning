from itertools import islice
from bs4 import BeautifulSoup
import urllib.request


def search():
    url = "https://en.wikipedia.org/wiki/Google"
    source_code = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code, "html.parser")

    body = soup.find('div', {'class': 'mw-parser-output'})
    file.write(str(body.text))


file = open('input.txt', 'a+', encoding='utf-8')
search()

f1 = open('input.txt')
f2 = open('input100lines.txt', 'a')
lines = list(islice(f1, 100))
f2.writelines(lines)

f1.close()
f2.close()

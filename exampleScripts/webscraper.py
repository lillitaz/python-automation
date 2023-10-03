import requests
import sys
import re
from bs4 import BeautifulSoup

url = sys.argv[1]
fileName = sys.argv[2]

# get the web page
html = requests.get(url).text

# parse the html using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# remove all script and style elements
for script in soup(["script", "style"]):
    script.extract()

# get the text
text = soup.get_text()

# remove any extra whitespace
text = re.sub(r'\s+', ' ', text)

# write the content to a markdown file
with open(f'../outputFiles/{fileName}', 'w') as f:
    f.write(text)
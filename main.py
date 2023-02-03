import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"


# Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)


# Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# HTML Tree Traversal
title = soup.title
# print(type(title)) # Tag
# print(type(title.string)) # String
# print(type(soup)) #BeautifulSoup
                   # Comment

# get the paras
paras = soup.find_all('p')
anchors = soup.find_all('a')

# print(paras)
# print(soup.find_all('p')['class'])
# print(soup.find_all('p', class_ = "lead"))

# print(soup.get_text())

for link in anchors:
    if(link != '#'):
        set.add("https://codewithharry.com" +link.get('href')) 
    
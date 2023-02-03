from bs4 import BeautifulSoup
import requests

# Connect to Website
try:
    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()
    
    soup  = BeautifulSoup(source.text,'html.parser')    
    movies = soup.find('tbody', class_="lister-list")
    movies = movies.find_all('tr')
    
    for movie in movies:
        name = movie.find('td', class_="titleColumn").a.text
        print(name)
        break
except Exception as e:
    print(e)
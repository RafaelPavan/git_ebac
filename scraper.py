import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

try:
    html = urlopen(url)
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be foun')

bs = BeautifulSoup(html, 'lxml')

movies = bs.select('.lister-list tr')

titles = []
directors = []
years = []
ratings = []

for movie in movies:
    titles.append(movie.find('td', class_='titleColumn').find('a').get_text())
    directors.append(movie.find('td', class_='titleColumn').find('a')['title'])
    years.append(movie.find('td', class_='titleColumn').find('span').get_text()[1:5])
    ratings.append(movie.find('td', class_='imdbRating').find('strong').get_text())

df = pd.DataFrame({
    "title": titles,
    "year" : years,
    "rating" : ratings,
    "director" : directors

})

print(df.head())

df.to_csv('melhores_filmes_imdb.csv')
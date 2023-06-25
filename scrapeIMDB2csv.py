from bs4 import BeautifulSoup
import requests
import csv

# open the file in the write mode
f = open('IMDB rating.csv', 'w')

columntitles = ['Movie rank', 'Movie name', 'Year of release', 'IMDB movie rating']

# create the csv writer
writer = csv.writer(f)

# write the header
writer.writerow(columntitles)

# To extract scraped data in english language
headers = {'Accept-Language': 'en-US,en;q=0.5'}

try:
    source = requests.get('https://www.imdb.com/chart/top/', headers=headers)
    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser')
    
    movies = soup.find('tbody', class_="lister-list").find_all('tr')
    
    
    for movie in movies:

        movie_name = movie.find('td', class_="titleColumn").a.text

        rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]

        year = movie.find('td', class_="titleColumn").span.text.strip('()')

        rating = movie.find('td', class_="ratingColumn imdbRating").strong.text
        print ( rank, movie_name, year, rating)

        movie_lst = [rank, movie_name, year, rating]
        
        # write a row to the csv file
        writer.writerow(movie_lst)
        

except Exception as e:
    print(e)

# close the file
f.close()
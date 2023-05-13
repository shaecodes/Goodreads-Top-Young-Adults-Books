from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

url = "https://www.goodreads.com/list/show/43.Best_Young_Adult_Books"

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content,"html.parser")
book_name = soup.find_all('tr', {'itemtype': 'http://schema.org/Book'})
books_data = []  # move this line outside the for loop

for book in book_name:
  book_link = book.find('a', {"class":"bookTitle"})['href']
  book_link = "https://www.goodreads.com/book" + book_link
  book_title = book.find_all('span', itemprop='name')[0].text
  book_author = book.find_all('span', itemprop='name')[1].text 
  book_rating = book.find('span', {"class":"minirating"}).text
  ratings = book_rating.split("—")

  try:
    avg_rating = float(ratings[0].split()[0])
    number_of_ratings = int(ratings[1].replace(',', '').split()[0])
  except ValueError:
    avg_rating = None
    number_of_ratings = None

  score_text = book.find('span', {"class":"smallText uitext"}).find('a', {"href":"#"}).text
  score = int(score_text.split(': ')[1].replace(',', ''))

  # append each book to the list
  books_data.append([book_title, book_author, avg_rating, number_of_ratings, score, book_link])

print(books_data)

with open('best_ya_books.csv', 'w', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(headers)
  writer.writerows(books_data)

table_headers = ["Title", "Author", "Average Rating", "Number of Ratings", "Score", "Links"]

with open('best_ya_books.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(table_headers)
    writer.writerows(books_data)

# print(f'Title: {book_title}')
# print(f'Author: {book_author}')
# print(f'Average Rating: {avg_rating}')
# print(f'Number of Ratings: {number_of_ratings}')
# print(f'Score: {score}')
# print(f'Link: {book_link}')
# print("\n")


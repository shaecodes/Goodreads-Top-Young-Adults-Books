# Goodreads Top Young Adult Books Scraper
This project is a Python script that scrapes the top young adult books on Goodreads and saves the book information in a CSV file. The script uses the BeautifulSoup library to parse the HTML of the book list page and extract the book title, author, score, average rating, number of ratings, and link.

## Getting Started
To run the script, you need to have Python 3 and the BeautifulSoup library installed on your computer. Once you have these requirements installed, you can simply run the goodreads_scraper.py file to start the scraping process.

## Usage
When you run the script, it will scrape the top young adult books on Goodreads and save the book information in a CSV file called best_ya_books.csv. The CSV file will contain one row for each book, with columns for the book title, author, score, average rating, number of ratings, and link.

After the script finishes running, you can open the CSV file in a spreadsheet program like Microsoft Excel or Google Sheets to view and analyze the book data. You can also load the CSV file into a pandas DataFrame in Python to perform further data manipulation and analysis.

## Contributing
If you find any bugs or issues with the script, or if you have any suggestions for improvement, feel free to create an issue or submit a pull request. We welcome contributions from the community!

# Any improvements?
- Add more exception handling 
- Allow opening of each url so that we can collect the genre, the year published, number of pages, other book recommendations, how many books the author has written and the first few lines of the description for each book. (This will mean creating multiple soups for each url so a more efficient library may be necessary. 

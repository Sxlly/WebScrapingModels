from bs4 import BeautifulSoup

with open('home.html', 'r') as scrape_file:
    content = scrape_file.read()
    print(content)

    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())
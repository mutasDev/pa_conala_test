#remove a div with a id `main-content` using beautifulsoup


from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')

main_content = soup.find(id="main-content")

main_content.decompose()
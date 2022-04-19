#BeautifulSoup find all 'span' elements in HTML string `soup` with class of 'starGryB sp'
 and extract the text from each of them.

for span in soup.find_all('span', class_='starGryB sp'):
    print(span.text)
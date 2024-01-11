import urllib3
from bs4 import BeautifulSoup

quote_page = "https://tahvel.edu.ee/#/timetable/38/generalTimetable/group"
page = urllib3.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('h1', attrs={'class': 'name'})
name = name_box.text.strip()
print (name)


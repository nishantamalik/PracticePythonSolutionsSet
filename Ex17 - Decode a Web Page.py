import requests
from bs4 import BeautifulSoup
url = 'https://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
texted = soup.find_all("h2",{"class" : "story-heading"})
for t in texted:
    if t.find("a"):
        print(t.a.text.strip())

https://gist.github.com/anonymous/94215829641cba607af7331ea884aa78
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')  # 드라이버를 실행합니다.

url = "https://careers.google.com/teams/facilities/"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get(url, headers=headers)

driver.get(url)  # 드라이버에 해당 url의 웹페이지를 띄웁니다.
sleep(2)  # 페이지가 로딩되는 동안 5초 간 기다립니다.

req = driver.page_source  # html 정보를 가져옵니다.
driver.quit()  # 정보를 가져왔으므로 드라이버는 꺼줍니다.

# soup = BeautifulSoup(data.text, 'html.parser')
soup = BeautifulSoup(req, 'html.parser')  # 가져온 정보를 beautifulsoup으로 파싱해줍니다.

songs = soup.select("#jump-content > main > div.gc-team-content > div:nth-child(2) > div > div > div > div.gc-grid > div")
print(len(songs))

#frm > div > table > tbody
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
#jump-content > main > div.gc-team-content > div:nth-child(2) > div > div > div > div.gc-grid > div:nth-child(1) > div > h4 > a

for song in songs:
    title = song.select_one("div").text.strip()
    print(title)
#jump-content > main > div.gc-team-content > div:nth-child(2) > div > div > div > div.gc-grid > div:nth-child(1)
#jump-content > main > div.gc-team-content > div:nth-child(2) > div > div > div > div.gc-grid > div:nth-child(2)
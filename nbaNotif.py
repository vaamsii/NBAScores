import pyttsx3

import win10toast 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

speaker = pyttsx3.init()

toaster = win10toast.ToastNotifier()

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.espn.com/nba/scoreboard")
hello = driver.find_element_by_id("sbpDate").text
print(hello)

speaker.say(hello)



table = driver.find_elements_by_id("teams")
length = len(table)

away = driver.find_elements_by_class_name("away")
home = driver.find_elements_by_class_name("home")
alen = len(away)
hlen = len(home)

awayList = []
homeList = []
awayScores = []
homeScores = []
names = driver.find_elements_by_class_name("sb-team-short")
scores = driver.find_elements_by_class_name("total")
slen = len(scores)
for x in range(0, alen, 2):
    atext = names[x].text
    awayList.append(atext)
for y in range(1, hlen, 2):
    htext = names[y].text
    homeList.append(htext)
for a in range(1, slen, 3):
    ascore = scores[a].text
    awayScores.append(ascore)
for b in range(2, slen, 3):
    hscore = scores[b].text
    homeScores.append(hscore)
for i in range(len(homeList)):
    p = f'{awayList[i]} {awayScores[i]} versus {homeList[i]} {homeScores[i]}'
    p2 = f'{awayScores[i]} to {homeScores[i]}'
    speaker.say(f'{awayList[i]} versus {homeList[i]}')
    speaker.say(f'{awayScores[i]} to {homeScores[i]}')
    print(p)
    toaster.show_toast('NBA SCORES', f'{awayList[i]} vs {homeList[i]}: {awayScores[i]} - {homeScores[i]}',duration=5)
    

speaker.runAndWait()


driver.quit()








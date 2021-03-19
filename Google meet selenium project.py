from selenium import webdriver
# import schedule
from selenium.webdriver.chrome.options import Options
from time import *

# from bs4 import BeautifulSoup
# import urllib.request as urllib2
# import re

opt = Options()
# opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2,
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2,
  })
# def thursday():
# from selenium.webdriver.common.keys import Keys

Path = "F:\\Coding shit\\Web Driver\\chromedriver.exe"
driver = webdriver.Chrome(Path)
# driver.get("https://classroom.google.com/")
# go_to_classroom = driver.find_element_by_xpath('//*[@id="gfe-main-content"]/section[1]/div/div/div/ul/li[2]/a/span')
# go_to_classroom.click()

sign_in = driver.get('https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
driver.maximize_window()  # Maximizes the window
# go_to_classroom.send_keys(Keys.CONTROL + '2')
# print(f'Title = {driver.title}')
# sleep(5)
# x = driver.switch_to.active_element

email_Path = driver.find_element_by_xpath('//*[@id="identifierId"]')
email_Path.click()
email_Path.send_keys('2019aryan.r.gupta@ves.ac.in')
nxt = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
nxt.click()
sleep(5)

Password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
Password.send_keys('censored hai lol')
sleep(3)

next_1 = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
next_1.click()
sleep(7)

# confirm = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/c-wiz/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div/span/span')
# confirm.click()
# driver.get("https://classroom.google.com/u/0/c/MjU5NjAwMzYyMjI2")
# sleep(5)

# PCOM classroom ka xpath
# pcom_clrm = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[2]/div/ol/li[11]/div[1]/div[3]/h2/a[1]/div[1]')
# pcom_clrm.click()
sleep(7)

pcom_clrm = driver.get('https://classroom.google.com/u/0/c/MjU5NjAwMzYyMjI2')
sleep(5)

# ss classroom ka link ka xpath
pcom_link = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/span/a/div')
pcom_link.click()
# extraction = ss_link.get_('href')
# print('SS link is' + extraction)
sleep(7)
# driver.switch_to.window(driver.window_handles[1])
current_tab = driver.window_handles[1]
driver.switch_to_window(current_tab)
print('58. This is ' + driver.title)
# current_tab = driver.window_handles[1]
# driver.get_window_position(current_tab)

# print(driver.title)
# After the tab of google meet open u get a button to dismiss the pop up...dismiss btn ka xpath
# window_after = driver.window_handles[1]
# driver.switch_to.window(window_after)
# html_page = urllib2.urlopen("https://classroom.google.com/c/MTI2MDM3NDU2OTUz")
# soup = BeautifulSoup(html_page)
# for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
#     print(link.get('href'))

# dismiss = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')
# driver.switch_to.frame(dismiss)
dismiss = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')
dismiss.click()
# # dismiss.sendKeys(Keys.ESCAPE)

join_now = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
join_now.click()

# thursday()
# schedule.every().thursday.at.('10:00').do(thursday())

# __________________________________________Classroom Stuff___________________________________________________
# tt for thu ss,mc, em, pce, pce lab

from selenium import webdriver
from datetime import datetime as dt
from selenium.webdriver.chrome.options import Options
from time import *

# creating chrome instance
from selenium.webdriver.common.keys import Keys

opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})

Path = "F:\\Coding shit\\Web Driver\\chromedriver.exe"
driver = webdriver.Chrome(chrome_options=opt, executable_path=Path)

email =  # Enter email here
password =  # Enter Password
def Sign_in():
    sign_in = driver.get(
        'https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    email_Path = driver.find_element_by_xpath('//*[@id="identifierId"]')
    email_Path.click()
    email_Path.send_keys(email)
    nxt = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
    nxt.click()
    sleep(5)

    Password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    Password.send_keys(Password)
    sleep(3)
    next_1 = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
    next_1.click()
    sleep(7)


def pcom():
    pcom_clrm = driver.get('https://classroom.google.com/u/0/c/MjU5NjAwMzYyMjI2')
    sleep(5)

    pcom_link = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/span/a/div')
    pcom_link.click()
    sleep(7)

    current_tab = driver.window_handles[1]
    driver.switch_to_window(current_tab)
    print('58. This is ' + driver.title)
    sleep(5)

    mic = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div')
    mic.click()
    sleep(2)

    cam = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div')
    cam.click()
    sleep(3)

    join_now = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
    join_now.click()
    sleep(10)


def ss():
    driver.get('https://classroom.google.com/u/1/c/MTI2MDM3NDU2OTUz')
    sleep(5)
    ss_link = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/span/a/div')
    ss_link.click()
    sleep(3)

    current_tab = driver.window_handles[1]
    driver.switch_to_window(current_tab)
    print('58. This is ' + driver.title)
    sleep(3)

    mic = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div')
    mic.click()
    sleep(2)

    cam = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div')
    cam.click()
    sleep(3)

    join_now = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
    join_now.click()
    sleep(10)


def mc():
    driver.get('https://classroom.google.com/u/0/c/MjU5NTYxMzMwODQw')
    mc_link = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/span/a/div')
    mc_link.click()

    current_tab = driver.window_handles[1]
    driver.switch_to_window(current_tab)
    print(driver.title)
    sleep(3)
    mic = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div')
    mic.click()
    sleep(2)

    cam = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div')
    cam.click()
    sleep(3)

    join_now = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div['
                                            '1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
    join_now.click()
    sleep(10)


def maths():
    driver.get('https://classroom.google.com/u/0/c/MjU5NTk3MzYzMTU5')
    sleep(5)

    maths_link = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/span/a/div')
    maths_link.click()

    current_tab = driver.window_handles[1]
    driver.switch_to_window(current_tab)
    print(driver.title)
    sleep(3)

    mic = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/span/a/div')
    mic.click()
    sleep(2)

    cam = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div['
        '2]/div/div')
    cam.click()
    sleep(3)

    join_now = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[''1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
    join_now.click()
    sleep(10)


                                                                                                # For Monday
while True:  # This while loop keeps checking continuously whether the time is reached or not
    if dt.today().weekday() == 0:
        if dt.today().hour == 10 and dt.today().minute == 00:
            Sign_in()
            pcom()
        if dt.today().hour == 11 and dt.today().minute == 00:  # Even if 00 is not written it will work form 10 am
            driver.quit()
        if dt.today().hour == 11 and dt.today().minute == 10:
            Sign_in()
            maths()
            if dt.today().hour == 12 and dt.today().minute == 10:
                driver.quit()
        if dt.today().hour == 12 and dt.today().minute == 20:
            Sign_in()
            mc()
            if dt.today().hour == 13 and dt.today().minute == 20:
                driver.quit()
        if dt.today().hour == 13 and dt.today().minute == 30:
            driver.quit()
            Sign_in()
            maths()
            if dt.today().hour == 14 and dt.today().minute == 30:
                driver.quit()

    if dt.today().weekday() == 1:                                                            # For Tuesday
        if dt.today().hour == 10 and dt.today().minute == 00:
            Sign_in()
            maths()
        if dt.today().hour == 11 and dt.today().minute == 00:  # Even if 00 is not written it will work form 10 am
            driver.quit()
        if dt.today().hour == 11 and dt.today().minute == 10:
            Sign_in()
            mc()
            if dt.today().hour == 12 and dt.today().minute == 10:
                driver.quit()
        if dt.today().hour == 12 and dt.today().minute == 20:
            Sign_in()
            pcom()
            if dt.today().hour == 13 and dt.today().minute == 20:
                driver.quit()
        if dt.today().hour == 13 and dt.today().minute == 30:
            driver.quit()
            Sign_in()
            ss()
            if dt.today().hour == 14 and dt.today().minute == 30:
                driver.quit()

    if dt.today().weekday() == 2:                                                         # For wednesday
        if dt.today().hour == 10 and dt.today().minute == 00:
            Sign_in()
            ss()
        if dt.today().hour == 11 and dt.today().minute == 00:  # Even if 00 is not written it will work form 10 am
            driver.quit()
        if dt.today().hour == 11 and dt.today().minute == 10:
            Sign_in()
            pcom()
            if dt.today().hour == 12 and dt.today().minute == 10:
                driver.quit()
        if dt.today().hour == 12 and dt.today().minute == 20:
            Sign_in()
            mc()
            if dt.today().hour == 13 and dt.today().minute == 20:
                driver.quit()
        if dt.today().hour == 13 and dt.today().minute == 30:
            driver.quit()
            Sign_in()
            maths()
            if dt.today().hour == 14 and dt.today().minute == 30:
                driver.quit()

    if dt.today().weekday() == 3:                                                           # For thursday
        if dt.today().hour == 10 and dt.today().minute == 00:
            Sign_in()
            pcom()
        if dt.today().hour == 11 and dt.today().minute == 00:  # Even if 00 is not written it will work form 10 am
            driver.quit()
        if dt.today().hour == 11 and dt.today().minute == 10:
            Sign_in()
            maths()
            if dt.today().hour == 12 and dt.today().minute == 10:
                driver.quit()
        if dt.today().hour == 12 and dt.today().minute == 20:
            Sign_in()
            mc()
            if dt.today().hour == 13 and dt.today().minute == 20:
                driver.quit()
        if dt.today().hour == 13 and dt.today().minute == 30:
            driver.quit()
            Sign_in()
            maths()
            if dt.today().hour == 14 and dt.today().minute == 30:
                driver.quit()
                                                                                                # For friday
    if dt.today().weekday() == 4:
        if dt.today().hour == 10 and dt.today().minute == 00:
            Sign_in()
            pcom()
        if dt.today().hour == 11 and dt.today().minute == 00:  # Even if 00 is not written it will work form 10 am
            driver.quit()
        if dt.today().hour == 11 and dt.today().minute == 10:
            Sign_in()
            maths()
            if dt.today().hour == 12 and dt.today().minute == 10:
                driver.quit()
        if dt.today().hour == 12 and dt.today().minute == 20:
            Sign_in()
            mc()
            if dt.today().hour == 13 and dt.today().minute == 20:
                driver.quit()
        if dt.today().hour == 13 and dt.today().minute == 30:
            driver.quit()
            Sign_in()
            maths()
            if dt.today().hour == 14 and dt.today().minute == 30:
                driver.quit()

    if dt.today().weekday() == 0:                                            # For friday.
        if dt.today().hour == 10 and dt.today().minute == 00:
            Sign_in()
            pcom()
        if dt.today().hour == 11 and dt.today().minute == 00:  # Even if 00 is not written it will work form 10 am
            driver.quit()
        if dt.today().hour == 11 and dt.today().minute == 10:
            Sign_in()
            maths()
            if dt.today().hour == 12 and dt.today().minute == 10:
                driver.quit()
        if dt.today().hour == 12 and dt.today().minute == 20:
            Sign_in()
            mc()
            if dt.today().hour == 13 and dt.today().minute == 20:
                driver.quit()
        if dt.today().hour == 13 and dt.today().minute == 30:
            driver.quit()
            Sign_in()
            ss()
            if dt.today().hour == 14 and dt.today().minute == 30:
                driver.quit()

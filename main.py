import selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


pin = input('enter the game pin: ')
nname = input('enter a nickname: ')

browser = webdriver.Firefox()

browser.get('http://www.kahoot.it')

# sleep(5)

gameId = browser.find_element_by_name('gameId')

gameId.send_keys(pin)
gameId.send_keys(Keys.RETURN)
sleep(2)
nickname = browser.find_element_by_name('nickname')
nickname.send_keys(nname)
#nickname.send_keys(Keys.RETURN)
submitbutton = browser.find_element_by_class_name("button__Button-c6mvr2-0")
submitbutton.click()
green = browser.find_elements_by_css_selector('div[color="#26890c"]')
sleep(2)

print('green found')
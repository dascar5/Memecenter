from selenium import webdriver
import time

browser = webdriver.Chrome()

#GLOBAL VARIABLES
page = 'https://www.memecenter.com/'
loginNotifCSS = '#fdc_ntfnotf > div.notification-icon.act_dropdownact'
usernameFieldCSS = '#l_username'
passwordFieldCSS = '#l_password'
loginCSS = '#login_form > div > div.npc-bottom > input'
username = 'your username'
password = 'your password'
addImageUrl = 'https://www.memecenter.com/addimage'
urlTextBox = '#m_imagelink'
url = 'url of pic you want to spam'
useAsIs = '#fdc_cropnext'
titleBox = '#m_title'
titleText = 'any title you choose'
tagsBox = 'm_tags'
tagsText = 'type any tags and separate them with comma,'
postNow = '#fdc_postnow'

#login
browser.get(page)
browser.maximize_window()
loginNotif = browser.find_element_by_css_selector(loginNotifCSS)
loginNotif.click()
usernameField = browser.find_element_by_css_selector(usernameFieldCSS)
usernameField.send_keys(username)
passwordField = browser.find_element_by_css_selector(passwordFieldCSS)
passwordField.send_keys(password)
login = browser.find_element_by_css_selector(loginCSS)
login.click()
time.sleep(2)

#spam loop
while True:
    browser.get(addImageUrl)
    pasteUrlBox = browser.find_element_by_css_selector(urlTextBox)
    pasteUrlBox.send_keys(url)
    time.sleep(3)
    UseAsIsButton = browser.find_element_by_css_selector(useAsIs)
    UseAsIsButton.click()
    title = browser.find_element_by_css_selector(titleBox)
    title.send_keys(titleText)
    tags = browser.find_element_by_name(tagsBox)
    tags.send_keys(tagsText)
    post = browser.find_element_by_css_selector(postNow)
    post.click()
    time.sleep(4)





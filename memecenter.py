from selenium import webdriver
import time

browser = webdriver.Chrome()

#GLOBAL VARIABLES
page = 'https://www.memecenter.com/fun/3377699729004745/the-fbi-is-coming-for-me/comments'
upvoteCSS = '#comments > div:nth-child(3) > div > table > tbody > tr > td:nth-child(2) > div.comment-buttons > div.upvote.act_comvote.login'
loginNotifCSS = '#fdc_ntfnotf > div.notification-icon.act_dropdownact'
usernameFieldCSS = '#l_username'
passwordFieldCSS = '#l_password'
loginCSS = '#login_form > div > div.npc-bottom > input'
password = 'asdasd'
logout = 'https://www.memecenter.com/auth/logout'
accounts = ['xxx1','xxx2','xxx3','xxx4','xxx5','xxx6','xxx7','xxx8','zzz1','zzz2','zzz3','zzz4','zzz5','zzz6',
            'zzz8','ccc1','ccc2','ccc3','ccc4','ccc5','ccc6','ccc7','ccc8','vvv1','vvv2','vvv3','vvv4','vvv5','vvv6',
            'vvv7','vvv8','bbb1','bbb2','bbb3','bbb4','bbb5','bbb6','bbb7','bbb8','nnn1','nnn2','nnn3','nnn4','nnn5',
            'nnn6','nnn7','nnn8','mmm1','mmm2','mmm3','mmm4','mmm5','mmm6','mmm7','mmm8',]

#script start
browser.get(page)
browser.maximize_window()

#loop
for i in accounts:
    loginNotif = browser.find_element_by_css_selector(loginNotifCSS)
    loginNotif.click()
    usernameField = browser.find_element_by_css_selector(usernameFieldCSS)
    usernameField.send_keys(i)
    passwordField = browser.find_element_by_css_selector(passwordFieldCSS)
    passwordField.send_keys(password)
    login = browser.find_element_by_css_selector(loginCSS)
    login.click()
    upvoteButton = browser.find_element_by_css_selector(upvoteCSS)
    upvoteButton.click()
    browser.get(logout)
    browser.get(page)









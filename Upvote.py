from selenium import webdriver

browser = webdriver.Chrome()

#GLOBAL VARIABLES
page = 'url of post where the comments are (make sure the url ends with /comments)'
upvoteCSS = '#comments > div:nth-child(3) > div > table > tbody > tr > td:nth-child(2) > div.comment-buttons > div.upvote.act_comvote.login'
loginNotifCSS = '#fdc_ntfnotf > div.notification-icon.act_dropdownact'
usernameFieldCSS = '#l_username'
passwordFieldCSS = '#l_password'
loginCSS = '#login_form > div > div.npc-bottom > input'
password = 'your password, make sure your password is same for all accounts'
logout = 'https://www.memecenter.com/auth/logout'
accounts = ['all usernames of your many accounts','keep them separate like this']

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









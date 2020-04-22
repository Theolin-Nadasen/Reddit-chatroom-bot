from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

#set headless mode on browser
firefox_headless = webdriver.FirefoxOptions()
firefox_headless.headless = True
browser = webdriver.Firefox(options=firefox_headless)


browser.get('REDDIT_CHAT_URL')
sleep(2)

#login
browser.find_element_by_id("loginUsername").send_keys("USERNAME")
browser.find_element_by_id("loginPassword").send_keys("PASSWORD")
browser.find_element_by_id("loginPassword").send_keys(Keys.RETURN)

#sending
sleep(20)
textbox = browser.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/form/textarea")

#get last message
def lastmsg():
    messages = browser.find_elements_by_class_name("_1q32G7u8aTwBaLUSN_06Cl")
    lastMessage = messages[-1].get_attribute("innerHTML")
    return lastMessage

#gets the last name
def lastname():
    name = browser.find_elements_by_class_name("pqdGGYoXaBuzfPrYLoqaM")
    name = name[-1].get_attribute("innerHTML")
    return name


# global variables
faqs= {}
comuser = ""


# commands

def dice():
    num = str(round(random.randint(1,6)))
    textbox.send_keys(num)
    textbox.send_keys(Keys.RETURN)
    return False

def close():
    if comuser == "_--_GOD_--_":
        return True
    else:
    	textbox.send_keys("you don't have permission to do that")
    	textbox.send_keys(Keys.RETURN)
    	return False

def addfaq():
    faqMsg = msg.split(" ", 2)
    faqs[faqMsg[1]] = faqMsg[2]
    textbox.send_keys("faq added with id {}".format(faqMsg[1]))
    textbox.send_keys(Keys.RETURN)
    return False

def faq():
    faqMsg = msg.split(" ", 2)
    if faqs.get(faqMsg[1]) != None:
        textbox.send_keys(faqs.get(faqMsg[1]))
        textbox.send_keys(Keys.RETURN)
    return False

def reverse():
    revtext = msg.split(" ", 1)
    revtext = revtext[1][::-1]
    textbox.send_keys(revtext)
    textbox.send_keys(Keys.RETURN)
    return False

def help():
    for key in cmds.keys():
        textbox.send_keys(key)
    textbox.send_keys(Keys.RETURN)
    return False

def myname():
    textbox.send_keys(lastname())
    textbox.send_keys(Keys.RETURN)
    return False



# add your commands to the dictionary

cmds = {"[dice]": dice, "[exit]": close, "[addfaq]": addfaq, "[faq]": faq, "[reverse]": reverse, "[help]": help, "[name]": myname}

while True:
    sleep(1)
    msg = lastmsg()
    comuser = lastname()
    x = msg.split(" ", 1)
    x = cmds.get(x[0])
    if x == None:
        stop = False
    else:
        stop = x()
    if stop:
        break

browser.quit()

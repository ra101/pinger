from os import system
from time import sleep, localtime, strftime
from random import random

# We are using selenium instead of requests module, 'cuz most website do not have features
# like getting data from command line or cURL due security reasons.
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

# connection probablity is 0.7 == 30%
if random() > 0.7 :
        
        # Sleep for ten minutes, before actually starting, one might connect to internet in that time.
        sleep(600)
        
        # list of websites, having them in .env is probably better
        # but i dont want another import just for this stupid program...
        websites = ["http://thewtvlist.epizy.com/home.html", "http://ra101.github.io/home.html"]

        options = Options()
        
        options.add_experimental_option('excludeSwitches', ['enable-logging']) # This stops echoing DevTools message.
        options.headless = True # duh!!
        try:
                driver = Chrome(options=options)
        except:
                os.system("choco update chromedriver -y") # I am a windows guy... for some reason... 
                driver = Chrome(options=options)
                
        system("echo %s > pinger.txt" % strftime("%d-%m-%Y %H:%M:%S", localtime())) # `>` to write the file, so instead of logs, it will have most recent one only.
        for site in websites:
                driver.get(site) # Boom!!
                system("echo %s >> pinger.txt" % site) # `>>` to append the file 
                sleep(60) # wait to load.
        driver.delete_all_cookies(); # imp!.. maybe... idk.
        driver.quit()
exit() # not imp, just there.

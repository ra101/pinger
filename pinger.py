from random import random
from os import system
from time import sleep, localtime, strftime

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

if random() > 0.7 :
        sleep(600)
        
        websites = ["http://thewtvlist.epizy.com/home.html", "http://ra101.github.io/home.html"]

        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.headless = True
        try:
                driver = Chrome(options=options)
        except:
                os.system("choco update chromedriver -y")
                driver = Chrome(options=options)
        system("echo %s > pinger.txt"%strftime("%Y-%m-%d %H:%M:%S", localtime()))
        for site in websites:
                driver.get(site)
                system("echo %s >> pinger.txt"%site)
                sleep(60) 
        driver.delete_all_cookies();
        driver.quit()
exit()

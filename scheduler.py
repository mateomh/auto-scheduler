import time
import os
from datetime import datetime, time as dt_time
from selenium import webdriver
from dotenv import load_dotenv

print(time.ctime())
load_dotenv()
site_url = os.environ.get('URL')

chrome_browser = webdriver.Chrome()

activation_time = dt_time(17,0,1)

script_done = False
while not script_done:
  current_time = datetime.now().time()
  if current_time == activation_time:
    chrome_browser.get(site_url)
    script_done = True

input("Press Enter to close the browser...")
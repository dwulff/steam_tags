import time, os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


# Instantiate an Options object
# and add the “ — headless” argument
opts = Options()
opts.add_argument(" — headless")
opts.add_argument("--start-maximized")

# Set the location of the webdriver
chrome_driver = os.getcwd() + "/0_materials/chromedriver"
driver = webdriver.Chrome(options=opts, executable_path=chrome_driver)

urls = open("1_data/urls.txt", "r")
urls = urls.readlines()
urls = [x.replace("\n","") for x in urls]

urls_ids = open("1_data/urls_ids.txt", "r")
urls_ids = urls_ids.readlines()
urls_ids = [x.replace("\n","") for x in urls_ids]

for i in range(len(urls)):

  driver.get(urls[i])
  time.sleep(3)
  
  select = Select(driver.find_element_by_xpath('//*[@id="table-apps_length"]/label/select'))
  
  # select by value 
  select.select_by_value('-1')
  
  time.sleep(5)
  
  out = open("1_data/sites/"+urls_ids[i]+".txt", "w")
  out.write(driver.page_source)


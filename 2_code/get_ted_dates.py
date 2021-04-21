import time, os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Instantiate an Options object
# and add the “ — headless” argument
opts = Options()
opts.add_argument(" — headless")
opts.add_argument("--start-maximized")

# Set the location of the webdriver
chrome_driver = os.getcwd() + "/0_materials/chromedriver"
driver = webdriver.Chrome(options=opts, executable_path=chrome_driver)

def get_ted_date(inds):
  
  for i in inds:
    
    print(i)
    
    url = "http://www.ted.com/talks/view/id/"
    driver.get(url + str(i))
    date = driver.find_element_by_xpath("//meta[@itemprop='uploadDate']").get_attribute("content")
    duration = driver.find_element_by_xpath("//meta[@itemprop='duration']").get_attribute("content")
  
    with open("1_data/ted_talks_dates/" + str(i) + ".txt","w") as to:
      to.write(date + "&&&&&" + duration)
  
      #print("went through")
  
      time.sleep(.5)

todo = []
with open('1_data/ted_date_todo.txt','r') as fl:
  for l in fl:
    todo.append(int(l))

get_ted_date(todo)
#get_ted([7230])

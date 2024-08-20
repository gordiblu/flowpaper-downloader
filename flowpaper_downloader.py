# import the required libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time as t

# run Chrome in headless mode
options = Options()
options.add_argument("--headless")

# start a driver instance
driver = webdriver.Chrome(options=options)
# set the browser window size
driver.set_window_size( 3840, 2160)
# last page
max_pages = 44
#url
url = "https://flowpaper.com/flipbook/https://flowpaper.com/example.pdf#page=1"
#images save path
path="images\\"

        
def screenshot(page_number, url):
    #wait t seconds until page is loaded
    #open the target website
    driver.get(url)
    t.sleep(4) #depending on resolution this may change, there are other smarter ways using selenium to wait for the page charge ...
  
    # get div1 element by ID | save into a folder previuously created 
    try:
        div_element = driver.find_element(By.ID, f"turn-page-wrapper-{page_number}")
        save_file = f"{page_number}.png"
        div_element.screenshot(f"{path}{save_file}")
    except: print(f"Failed to save page {page_number}...")
    
    # get div2 element by ID | save into a folder previuously created 
    try:
        div_element2 = driver.find_element(By.ID, f"turn-page-wrapper-{page_number+1}")
        save_file2 = f"{page_number+1}.png"
        div_element2.screenshot(f"{path}{save_file2}")
    except: print(f"Failed to save page {page_number+1}...")
    
  
if __name__ == "__main__":  
    # this sequence Iter starting on 1 by 2: 1,2,4,6,8 ... play with this in case you need
    sequence = [1]
    i = 2
    while i <= max_pages:
        sequence.append(i)
        i += 2
    #print(sequence)
    #delete url  page tag if needed
    if "#page=" in url: url = url.split("#page=")[0]
    else: None
    url_parse = ""
   
    for page in sequence:
        url_parse = url+f"#page={page}"
        print(f"url: {url_parse}")
        screenshot(page, url_parse)
        
    # quit the browser
    driver.quit()

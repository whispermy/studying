from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

marvel = ["cris evans", "robert downey jr", "cris hemsworth", 
          "tom holland", "hulk", "James Rupert Rhodes", "Scarlett Johansson",
          "marvel vision", "Samuel Thomas Wilson", "Jeremy Renner", "Wanda Maximoff",
          "antman", "t challa", "nick fury", "Virginia Potts", "Maria Hill",
          "James Buchanan Barnes", "Pietro Maximoff", "Hope van Dyne", 
          "Okoye", "Shuri", "Carol Susan Jane Danvers", "Peter Jason Quill",
          "Gamora", "Drax", "marvel rocket","Groot", "marvel Mantis", "marvel Nebula",
          "Yondu Udonta", "Stephen Vincent Strange"]

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")

basic_path = "C:\\Users\\dlfhq\\Documents\\GitHub\\jocodingpractice\\selenium\\machine_images\\"

for marvel_count in range(1,31):
        try:
                
                elem = driver.find_element_by_name("q")
                elem.send_keys(marvel[marvel_count])
                elem.send_keys(Keys.RETURN)

                my_path = basic_path + marvel[marvel_count]

                try:
                        if not(os.path.isdir(my_path)):
                                os.makedirs(os.path.join(my_path))
                except OSError as e:
                        if e.errno != errno.EEXIST:
                                print("Failed to create directory!!!!!")
                                raise


                SCROLL_PAUSE_TIME = 1

                # Get scroll height
                last_height = driver.execute_script("return document.body.scrollHeight")

                while True:
                        # Scroll down to bottom
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                        # Wait to load page
                        time.sleep(SCROLL_PAUSE_TIME)

                        # Calculate new scroll height and compare with last scroll height
                        new_height = driver.execute_script("return document.body.scrollHeight")        
                        if new_height == last_height:
                                try:
                                        driver.find_element_by_css_selector(".mye4qd").click()
                                except:
                                        break 
                        last_height = new_height

                images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
                count = 1;

                opener=urllib.request.build_opener()
                opener.addheaders=[('User-Agent','Chrome/36.0.1941.0')]
                urllib.request.install_opener(opener)

                for image in images:
                        try: 
                                image.click()
                                time.sleep(2)
                                imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")
                                #print(imgUrl)
                                onefilename = str(count)+"test.jpg"
                                fullfilename = os.path.join(my_path, onefilename)
                                urllib.request.urlretrieve(imgUrl, fullfilename)
                                #urllib.request.urlretrieve(imgUrl, str(count) + "test.jpg")
                                count = count + 1
                        except:
                                pass
        
        except:
                pass


driver.close()
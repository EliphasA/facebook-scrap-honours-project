from facebook_page_scraper import Facebook_scraper
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
import pandas as pd

page_list = ["TelecomNamibia"]

proxy_port = 10001
post_counts = 100
browser = 'firefox'
timeout = 600
headless = False

def facebook_scraper(page_list,proxy_port,post_counts,browser,timeout,headless): 
    for page in page_list:
        proxy = f'username:password@us.smartproxy.com:{proxy_port}'
        
        scraper = Facebook_scraper(page,post_counts,browser,proxy=proxy,timeout=timeout,headless=headless)
        
        json_data = scraper.scrap_to_json()
        
        print(json_data)
        
        proxy_port += 1
        
        return scraper.scrap_to_json()
    
# Function to get facebook post comments
def get_post_comment(post_url_list):
    # Set up the Chrome WebDriver
    driver = webdriver.Firefox(service=Service(executable_path='C:/Program Files/Mozilla Firefox/geckodriver.exe'))

    # Open Facebook and log in
    driver.get('https://www.facebook.com')
    email = 'andreaelifasshikongo1@gmail.com'
    password = 'Elifas@02'

    email_field = driver.find_element_by_id('email')
    password_field = driver.find_element_by_id('pass')

    email_field.send_keys(email)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    
    #comments array
    comments_content = []
    comment_author = []
    
    for post_url in post_url_list:
        # Navigate to the post
        driver.get(post_url)

        # Scroll to load comments (you may need to adjust the scrolling logic)
        for _ in range(5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        # Extract comments
        # comments = driver.find_elements_by_css_selector('[data-ad-preview="message"]')
        authors = driver.find_elements(By.CSS_SELECTOR,"span[class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa x1s688f xzsf02u']")
        comments = driver.find_elements(By.CSS_SELECTOR,"div[class='xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs']")
        

        for comment in comments:
            print(comment.text)
            comments_content.append(comment.text)
            
        for author in authors:
            print("Author: ",author.text)
            comment_author.append(author.text)
    df = pd.DataFrame({"comment_author":comment_author,"comment_content":comments_content})
    return df

    # Close the WebDriver
    # driver.quit()
    
    
    
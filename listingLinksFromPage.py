from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

url = 'https://www.songtive.com/en/chords/piano/C'  # Substitua pela URL correta
driver.get(url)

time.sleep(5)

elements = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]//a')

links = [element.get_attribute('href') for element in elements]

with open('OUTPUTS/links.txt', 'w') as file:
    for link in links:
        if link:
            file.write(f"{link}\n")

driver.quit()

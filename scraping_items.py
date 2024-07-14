from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def save_content_to_file(content, filename="OUTPUTS/output.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(content + "\n")

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    with open("links.txt", "r", encoding="utf-8") as f:
        links = f.readlines()
        print(links)

    for link in links:
        url = link.strip()
        print(url)
        if url:
            driver.get(url)

            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/div/div[3]/div[1]/div/div/div[1]'))
                )
                content = element.text

                print(content)
                save_content_to_file(content)
            except Exception as e:
                print(f"Error while url capturing {url}: {e}")

finally:
    driver.quit()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

userinput = input("What is Your Pathway?: ")
chrome_options = Options()
chrome_options.add_argument("--headless")
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)
url = "https://ai-roadmap.com/"
driver.get(url)
sleep(30)
input_field = driver.find_element(
    By.ID, 'react-aria-1')
input_field.clear()
input_field.send_keys(userinput)

button = driver.find_element(By.XPATH, "/html[@class='dark-theme']/body/div[@id='__next']/div[2]/div[@class='nextui-c-bsxZDy']/div[@class='nextui-c-fdHeMm nextui-c-fdHeMm-dwxLNB-responsive-true nextui-c-fdHeMm-iizPHCF-css']/div[@class='nextui-c-kRHeuF nextui-c-kRHeuF-ijDEIix-css nextui-grid-item nextui-grid-container content']/div[@class='nextui-c-kRHeuF nextui-c-kRHeuF-ibBQlvc-css nextui-grid-item xs sm md lg xl'][1]/div[@class='box']/div[@class='nextui-c-ceYOvq']/div[@class='nextui-c-BDLTQ nextui-c-jMTBsW nextui-c-gulvcB nextui-c-BDLTQ-eZMbDJ-variant-shadow nextui-c-BDLTQ-fmlsco-borderWeight-light nextui-c-BDLTQ-cuwTXc-disableAnimation-false card']/form/div[@class='formContainer']/div[2]/button[@class='nextui-c-iWjDFM nextui-c-gulvcB nextui-c-iWjDFM-hkKLfu-color-default nextui-c-iWjDFM-fbAdQA-size-lg nextui-c-iWjDFM-cwXrJp-borderWeight-normal nextui-c-iWjDFM-iPJLV-css nextui-button nextui-button--ready nextui-c-bBkWuD submitButton']")
button.click()
sleep(70)  # Replace with the class name of the resulting content
page_source = driver.page_source

# Close the browser
driver.quit()

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')
divs_hello = soup.find_all('div', class_='styles_nodeOtherLevel__SZmQG')
with open('test.txt', 'w') as file:
    # Iterate over the div elements and write their text to the file
    for div_hello in divs_hello:
        inner_div_text = div_hello.find('div').text
        file.write(inner_div_text + '\n')

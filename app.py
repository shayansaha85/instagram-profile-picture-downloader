from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome(executable_path="driver/chromedriver.exe", chrome_options=options)

instagram_username = "shayansaha85" #ENTER THE INSTAGRAM USERNAME

profile_url = f"https://www.instagram.com/{instagram_username}"

driver.get(profile_url)

xpath_dp = "/html/body/div[1]/div/div/section/main/div/header/div/div/div/button/img"
img = driver.find_element_by_xpath(xpath_dp)

src = img.get_attribute('src')

urllib.request.urlretrieve(src, f"{instagram_username}.png")

driver.close()
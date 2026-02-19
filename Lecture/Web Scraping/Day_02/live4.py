from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_argument("--no-level=3")

print("브라우저를 실행합니다...")
driver = webdriver.Chrome(options=chrome_options)

url = "https://www.coupang.com/"
driver.get(url)
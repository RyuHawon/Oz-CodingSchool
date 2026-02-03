from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

options = webdriver.ChromeOptions()

# 1. 크롬 옵션에서 최대한 사람처럼
options = Options()

my_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
options.add_argument(f"user-agent={my_user_agent}")
options.add_experimental_option("detach", True)

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("lang=ko_KR")

driver = webdriver.Chrome(options=options)

# 2. 봇 감지 우회 스크립트
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

url = "https://www.coupang.com/"

wait = WebDriverWait(driver, 10)
search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.headerSearchKeyword")))

search_input.click()
search_input.send_keys("페브리즈")
search_input.send_keys(Keys.ENTER)

time.sleep(3)

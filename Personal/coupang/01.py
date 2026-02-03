from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()

# 1. 자동화 제어 흔적 제거
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

# 2. 유저 에이전트 설정
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")

chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# 4. navigator.webdriver 속성을 false 로 변경하는 스크립트
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """})

url = "https://www.coupang.com/np/search?q=페브리즈"
driver.get(url)
time.sleep(3)

print("과연?")
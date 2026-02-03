from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_argument("--no-level=3")

print("브라우저를 실행합니다...")
driver = webdriver.Chrome(options=chrome_options)

url = "https://kream.co.kr/"
driver.get(url)
sleep(1)

driver.find_element(By.CSS_SELECTOR, "button.btn_search").click()
sleep(1)
input_tag = driver.find_element(By.CSS_SELECTOR, "input.input_search")
input_tag.send_keys("슈프림")
input_tag.send_keys(Keys.ENTER)
sleep(1)

for i in range(1):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1.5)

html = driver.page_source
html = BeautifulSoup(html, "lxml")
wrapper = html.find("div", {"class": "layout-grid-horizontal-equal"})
items = wrapper.find_all("a", {"class": "product_card"})
for item in items:
    product_link = "https://kream.co.kr" + item.get("href").strip()
    product_detail_div = item.find("div", {"class": "layout_list_vertical"})
    product_strings = [p.get_text(strip=True) for p in product_detail_div.find_all("p")]
    
    if len(product_strings) < 6:
        continue
    
    brand, name, price, likes, review, trade = product_strings

    if "후드" in product_strings[1]:
        print("==========================")
        print(product_link)
        print(
            brand,
            name,
            price,
            likes,
            review,
            trade,
        )


# counter = 0
# while counter <= 10:
#     driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.PAGE_DOWN)
#     sleep(1.5)
#     counter += 1
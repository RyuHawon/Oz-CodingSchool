from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

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

for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1.5)

html = driver.page_source
html = BeautifulSoup(html, "lxml")
wrapper = html.find("div", {"class": "layout-grid-horizontal-equal"})
items = wrapper.find_all("a", {"class": "product_card"})
product_links: list[str] = list()

for item in items:
    product_link = "https://kream.co.kr" + item.get("href").strip()
    product_links.append(product_link)
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

driver.quit()

def fetch_product_page(link: str):
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://kream.co.kr/?utm_source=google&utm_medium=cpc&utm_campaign=NEW_%EC%9E%90%EC%82%AC%EB%AA%85_%EC%88%98%EB%8F%99_PC&utm_term=%ED%81%AC%EB%A6%BC&utm_content=A.+%EC%9E%90%EC%82%AC%EB%AA%85_%EC%88%98%EB%8F%99&gad_source=1&gad_campaignid=20153300613&gbraid=0AAAAACRs-HtUIT5Xw1IGWEvbYd3LcVFOk&gclid=CjwKCAiAs4HMBhBJEiwACrfNZdGFUoPkvXfTn1EVnxugH_pLQ-JYwXaxnFPOB4cWJ3nocUIdtAszuRoCv6MQAvD_BwE',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    # 'cookie': 'webDid=7a731056-24e1-4deb-87e4-d73501f9e78e; _fwb=150hlFtNuf4FagKqOuKBB0U.1768288810459; ab180ClientId=6231f21f-5dbc-46c2-a868-53442b9452cf; airbridge_device_alias__kream=%7B%22amplitude_device_id%22%3A%22ee42f2d7-6983-4242-b9c4-6367a7b1062f%22%7D; airbridge_migration_metadata__kream=%7B%22version%22%3A%221.11.1%22%7D; _gid=GA1.3.2078664038.1770083599; strategy=local; ticketExpire=0; AMP_MKTG_487619ef1d=JTdCJTIydXRtX2NhbXBhaWduJTIyJTNBJTIyTkVXXyVFQyU5RSU5MCVFQyU4MiVBQyVFQiVBQSU4NV8lRUMlODglOTglRUIlOEYlOTlfUEMlMjIlMkMlMjJ1dG1fY29udGVudCUyMiUzQSUyMkEuJTIwJUVDJTlFJTkwJUVDJTgyJUFDJUVCJUFBJTg1XyVFQyU4OCU5OCVFQiU4RiU5OSUyMiUyQyUyMnV0bV9tZWRpdW0lMjIlM0ElMjJjcGMlMjIlMkMlMjJ1dG1fc291cmNlJTIyJTNBJTIyZ29vZ2xlJTIyJTJDJTIydXRtX3Rlcm0lMjIlM0ElMjIlRUQlODElQUMlRUIlQTYlQkMlMjIlMkMlMjJyZWZlcnJlciUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGd3d3Lmdvb2dsZS5jb20lMkYlMjIlMkMlMjJyZWZlcnJpbmdfZG9tYWluJTIyJTNBJTIyd3d3Lmdvb2dsZS5jb20lMjIlMkMlMjJnYnJhaWQlMjIlM0ElMjIwQUFBQUFDUnMtSHRVSVQ1WHcxSUdXRXZiWWQzTGNWRk9rJTIyJTJDJTIyZ2NsaWQlMjIlM0ElMjJDandLQ0FpQXM0SE1CaEJKRWl3QUNyZk5aZEdGVW9Qa3ZYZlRuMUVWbnh1Z0hfcExRLUpZd1hheG5GUE9CNGNXSjNub2NVSWR0QXN6dVJvQ3Y2TVFBdkRfQndFJTIyJTdE; web_to_app_dismiss=false; _gcl_gs=2.1.k1$i1770093671$u65969396; _gac_UA-153398119-1=1.1770093675.CjwKCAiAs4HMBhBJEiwACrfNZdGFUoPkvXfTn1EVnxugH_pLQ-JYwXaxnFPOB4cWJ3nocUIdtAszuRoCv6MQAvD_BwE; _gat_gtag_UA_153398119_1=1; airbridge_utm__kream=%7B%22channel%22%3A%22google%22%2C%22parameter%22%3A%7B%22medium%22%3A%22cpc%22%2C%22campaign%22%3A%22NEW_%uC790%uC0AC%uBA85_%uC218%uB3D9_PC%22%2C%22term%22%3A%22%uD06C%uB9BC%22%2C%22content%22%3A%22A.+%uC790%uC0AC%uBA85_%uC218%uB3D9%22%7D%7D; airbridge_utm_url__kream=https%3A//kream.co.kr/%3Futm_source%3Dgoogle%26utm_medium%3Dcpc%26utm_campaign%3DNEW_%25EC%259E%2590%25EC%2582%25AC%25EB%25AA%2585_%25EC%2588%2598%25EB%258F%2599_PC%26utm_term%3D%25ED%2581%25AC%25EB%25A6%25BC%26utm_content%3DA.+%25EC%259E%2590%25EC%2582%25AC%25EB%25AA%2585_%25EC%2588%2598%25EB%258F%2599%26gad_source%3D1%26gad_campaignid%3D20153300613%26gbraid%3D0AAAAACRs-HtUIT5Xw1IGWEvbYd3LcVFOk%26gclid%3DCjwKCAiAs4HMBhBJEiwACrfNZdGFUoPkvXfTn1EVnxugH_pLQ-JYwXaxnFPOB4cWJ3nocUIdtAszuRoCv6MQAvD_BwE; airbridge_utm_timestamp__kream=1770093675102; wcs_bt=s_59a6a417df3:1770093681; i18n_redirected=ko; _gcl_aw=GCL.1770093682.CjwKCAiAs4HMBhBJEiwACrfNZdGFUoPkvXfTn1EVnxugH_pLQ-JYwXaxnFPOB4cWJ3nocUIdtAszuRoCv6MQAvD_BwE; _ga_SRFKTMTR0R=GS2.1.s1770093674$o4$g1$t1770093681$j53$l0$h0; _ga_5LYDPM15LW=GS2.1.s1770093674$o4$g1$t1770093681$j53$l0$h0; _ga=GA1.3.1237372966.1768288811; airbridge_session__kream=%7B%22id%22%3A%22bcb9f659-e225-4b88-b9d2-ef334712095d%22%2C%22timeout%22%3A1800000%2C%22start%22%3A1770093675109%2C%22end%22%3A1770093681911%7D; AMP_487619ef1d=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJlZTQyZjJkNy02OTgzLTQyNDItYjljNC02MzY3YTdiMTA2MmYlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzcwMDkzNjczMzcwJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTc3MDA5MzY4MjE4OSUyQyUyMmxhc3RFdmVudElkJTIyJTNBNTUlMkMlMjJwYWdlQ291bnRlciUyMiUzQTAlN0Q=',
}
    
    try:
        res = requests.get(link, timeout=5)
        res.raise_for_status()
        return res.content[100:200]
    except Exception as e:
        print(f"에러 발생 >> {e}")

results = list()

with ThreadPoolExecutor(max_workers=4) as ex:
    futures = [ex.submit(fetch_product_page, link) for link in product_links]

    for fut in as_completed(futures):
        try:
            results.append(fut.result())
        except Exception as e:
            print(f"에러 발생 >> {e}")


headers = {
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'baggage': 'sentry-environment=production,sentry-release=service-new%3Aproduction%40undefined,sentry-public_key=5f09575751fcc1ac319fcca40a4fd049,sentry-trace_id=eee2c122d4ca4ee4a4692e5c27fc7b1b,sentry-sample_rand=0.8504020293286325,sentry-sample_rate=0.005',
    'origin': 'https://kream.co.kr',
    'priority': 'u=1, i',
    'referer': 'https://kream.co.kr/products/768631',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sentry-trace': 'eee2c122d4ca4ee4a4692e5c27fc7b1b-b6392f349de18bb3-0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    'x-kream-api-version': '53',
    'x-kream-client-datetime': '20260203135130+0900',
    'x-kream-device-id': 'web;7a731056-24e1-4deb-87e4-d73501f9e78e',
    'x-kream-web-build-version': '26.1.2',
    'x-kream-web-request-secret': 'kream-djscjsghdkd',
}

params = {
    'request_key': '18fbf3c2-85ee-4a5c-9018-6b0df7fb5d58',
}

res = requests.get(
    'https://api.kream.co.kr/api/fetch/related-recommended-items/768631',
    params=params,
    headers=headers,
)

result = res.json()
print(result)


# counter = 0
# while counter <= 10:
#     driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.PAGE_DOWN)
#     sleep(1.5)
#     counter += 1
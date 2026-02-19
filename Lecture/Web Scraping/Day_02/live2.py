import json
import requests
from bs4 import BeautifulSoup

url = "https://blog.naver.com/PostView.naver"
payload = {
    "blogId": "pororin_hamong",
    "logNo": "224162984703",
    "redirect": "Dlog",
    "widgetTypeCall": "true",
    "noTrackingCode": "true",
    "directAccess": "false"
}

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}

res = requests.get(url, params=payload, headers=headers)
res.raise_for_status()
html = BeautifulSoup(res.content, "lxml")
all_imgs = html.find_all("a", {"class": "se-module-image-link"})
for a in all_imgs:
    data: dict = json.loads(a.get("data-linkdata"))
    print(data.get("src"))
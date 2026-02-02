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

outter_target = html.find("div", {"class": "se-main-container"})
blocks = outter_target.find_all("div", {"class": "se-component"})

comp_text_list = []
comp_img_list = []

for comp in blocks:
    class_list = comp.get("class")
    if "se-text" in class_list:
        comp_text_list.append(comp.get_text(strip=True))

    elif "se-image" in class_list:
        img_tag = comp.select_one("img")
        if not img_tag:
            continue

        img_src = (
            img_tag.get("data-lazy-src").strip()
            if img_tag.get("data-lazy-src")
            else img_tag.get("src").strip()
        )
        comp_img_list.append(img_src)
    
    elif "se-imageStrip" in class_list:
        img_tags = comp.find_all("img")
        img_srcs = [img_tag.get("data-lazy-src") or img_tag.get("src")
        for img_tag in img_tags]
        comp_img_list.extend(img_srcs)

print(comp_img_list)


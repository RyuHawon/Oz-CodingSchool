from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup

@dataclass
class Item:
    birth: str
    physical: str
    team: str
    family: str
    start: str
    real: str
    site: str
    activity: str


url = "https://search.naver.com/search.naver"
params = {
    "where": "nexearch",
    "sm": "top_hty",
    "fbm": "0",
    "ie": "utf8",
    "query": "손흥민",
    "ackey": "ps3lzxvq",
}

res = requests.get(url, params=params)
res.raise_for_status()
html = BeautifulSoup(res.content, "lxml")

target = html.find("section", {"class": ["sc_new", "cs_common_module", "case_normal", "_au_people_content_wrap"]})
real_target = target.select_one("div.cm_info_box")
all_dds = real_target.select("dd")

team_link = all_dds[2].select_one("a").get("href")
site_link = all_dds[6].select_one("a").get("href")


Item(
    birth=all_dds[0].get_text(strip=True),
    physical=all_dds[1].get_text(strip=True),
    team=all_dds[2].get_text(strip=True),
    family=all_dds[3].get_text(strip=True),
    start=all_dds[4].get_text(strip=True),
    real=all_dds[5].get_text(strip=True),
    site=all_dds[6].get_text(strip=True),
    activity=all_dds[7].get_text(strip=True),
)

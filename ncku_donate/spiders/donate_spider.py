import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DonateSpider(scrapy.Spider):
    name = "donate_spider"
    allowed_domains = ["donate.ncku.edu.tw"]
    start_urls = ["https://donate.ncku.edu.tw/p/405-1055-214886,c2043.php?Lang=zh-tw"]
    #請在start_utls內貼上您想爬取的該年份芳名錄網址，預設為2025年

    def __init__(self):
        options = Options()
        options.add_argument("--headless") 
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=options)

    def parse(self, response):
        self.driver.get(response.url)

        iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
        if iframes:
            print("發現 iframe，切換到第一個 iframe")
            self.driver.switch_to.frame(iframes[0]) 
            time.sleep(3)  

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "tr.odd, tr.even"))
        )

        rows = self.driver.find_elements(By.CSS_SELECTOR, "tr.odd, tr.even")
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            if len(columns) >= 4:
                yield {
                    "date": columns[0].text.strip(),
                    "donor": columns[1].text.strip(),
                    "amount": columns[2].text.strip(),
                    "purpose": columns[3].text.strip(),
                }

    # 切回主畫面
        self.driver.switch_to.default_content()

        def closed(self, reason):
            self.driver.quit() 

# 執行請在終端機，本專案目錄輸入scrapy crawl donate_spider -o data/年份donations.csv


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

keywords = ["shoes", "shirts", "bags", "watches", "phones"]

headers = {
    "User-Agent": "Mozilla/5.0"
}

data = []

for keyword in keywords:
    for page in range(1, 6):  # 5 صفحات لكل keyword
        url = f"https://www.jumia.com.eg/catalog/?q={keyword}&page={page}"

        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        products = soup.select("article.prd")

        for product in products:
            name = product.select_one("h3")
            price = product.select_one(".prc")
            link = product.find("a", href=True)
            image = product.select_one("img")

            product_link = None
            if link:
                product_link = "https://www.jumia.com.eg" + link["href"]

            image_link = None
            if image:
                image_link = image.get("data-src") or image.get("src")

            if name and price:
                data.append({
                    "name": name.text.strip(),
                    "price": price.text.strip(),
                    "link": product_link,
                    "image": image_link,
                    "category": keyword
                })

        time.sleep(1)  # مهم جدًا عشان ما يتعملكش block

df = pd.DataFrame(data)
df.to_csv("products.csv", index=False, encoding="utf-8")

print("Total products scraped:", len(data))
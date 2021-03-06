import os, bs4, json
import urllib.request, urllib.error
import requests
from bs4 import BeautifulSoup

keywords = ['Shibainu', 'Chihuahua', 'Golden Retriever']

image_count = 300

class Google(object):
    def __init__(self):
        self.GOOGLE_SEARCH_URL = "https://www.google.co.jp/search"
        self.session = requests.session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)  \
                AppleWebKit/537.36 (KHTML, like Gecko)  \
                Chrome/43.0.2357.134 Safari/537.36"
            }
        )

    def search(self, keyword, maximum):
        print(f"Begining searching {keyword}")
        query = self.query_gen(keyword)
        return self.image_search(query, maximum)

    def query_gen(self, keyword):

        page = 0
        while True:
            params = urllib.parse.urlencode(
                {"q": keyword, "tbm": "isch", "ijn": str(page)}
            )

            yield self.GOOGLE_SEARCH_URL + "?" + params
            page += 1

    def image_search(self, query_gen, maximum):
        results = []
        total = 0
        while True:
            html = self.session.get(next(query_gen)).text
            soup = BeautifulSoup(html, "html.parser")
            elements = soup.select(".rg_meta.notranslate")
            jsons = [json.loads(e.get_text()) for e in elements]
            image_url_list = [js["ou"] for js in jsons]

            if not len(image_url_list):
                print("-> No more images")
                break
            elif len(image_url_list) > maximum - total:
                results += image_url_list[: maximum - total]
                break
            else:
                results += image_url_list
                total += len(image_url_list)

        print("-> Found", str(len(results)), "images")
        return results

def main():
    google = Google()

    results = google.search(keyword, maximum=image_count)
    print(results)

for keyword in keywords:
    print("download now ...",  keyword)

    save_directory = "./dataset/" + keyword
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
        
    main()
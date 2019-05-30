import requests
from bs4 import BeautifulSoup

# while True:
for a in range(5):
    url = requests.get("https://turbo.az/")


src = url.content
soup = BeautifulSoup(src, 'html.parser')

# links = soup.find_all("div", class_='page-content')

# urls = []

# for link in soup.find_all("div", class_="page-content"):
#     if "products-i-link" in link:
#         urls.append(link)

if __name__ == '__main':
    retrieve_all_cars()

# print(urls)

def retrieve_all_cars():
    print(soup.find_all("div", class_="page-content"))




retrieve_all_cars()



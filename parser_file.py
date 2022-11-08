from bs4 import BeautifulSoup
import requests
from data.loader import db

class OpenShopParser:
    def __init__(self, category):
      self.category = category.lower()
      self.URL = 'https://alijahon.uz/category/'

    def get_soup(self):
        try:
            response = requests.get(self.URL + self.category)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        except:
            print('404')

    def get_info(self):
        data = []
        soup = self.get_soup()
        box = soup.find('div', class_='row')
        products = box.find_all('div', class_="col-6 mb-3 col-md-6 col-lg-4")
        for product in products:
            title = product.find('h5').get_text(strip=True)
            link = 'https://alijahon.uz' + product.find('a')['href']
            price = int(product.find('h5', class_="fs-md-2 text-warning mb-0 d-flex align-items-center mb-2").get_text(strip=True).split('so\'m')[0].replace(' ', ''))
            image ='https://alijahon.uz' +  product.find('img')['src']

            cat_id = db.select_category_id_by_cat_name(self.category)[0]

            data.append({
                'title': title,
                'link': link,
                'price': price,
                'image': image,
                'category_id': cat_id
            })
        return data
        # print(product)
        #     print(title, price, link, image)

# product = OpenShopParser('uy-uchun')
# product.get_info()

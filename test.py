from data.loader import bot, db
from parser_file import OpenShopParser as OP
# from pprint import pprint
from parser_file import OpenShopParser


db.create_categories_table()
db.create_products_table()

db.insert_categories('uy-uchun')
db.insert_categories('bolalar-uchun')
db.insert_categories('sovga')
db.insert_categories('ayollar')
db.insert_categories('davolovchi-mahsulotlar')
db.insert_categories('erkaklar-uchun')
db.insert_categories('fitnes')
db.insert_categories('davolovchi-mazlar')
db.insert_categories('moshina-uchun')

sovga = OpenShopParser('uy-uchun')
# pprint(sovga.get_info())

products_list = [OP('uy-uchun').get_info(), OP('bolalar-uchun').get_info(), OP('sovga').get_info(),
                 OP('ayollar').get_info(), OP('davolovchi-mahsulotlar').get_info(), OP('erkaklar-uchun').get_info(),
                 OP('fitnes').get_info(), OP('davolovchi-mazlar').get_info(), OP('moshina-uchun').get_info()]


for products in products_list:
    for product in products:
        product_name = product['title']
        product_link = product['link']
        product_price = product['price']
        product_image = product['image']
        category_id = product['category_id']

        print(product_name)
        print('1')
        print(product_link)
        print('2')
        print(product_price)
        print('3')
        print(product_image)
        print('4')
        print(category_id)
        print('5')

        db.insert_products(product_name, product_link, product_price, product_image, category_id)


# print(db.select_products_by_pagination(1, 12, 6))
#
# print(db.count_products_by_category_id(1))

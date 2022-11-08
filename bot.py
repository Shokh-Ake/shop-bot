'''
BOTNI ISHGA TUSHIRISH
'''
from middlewares import SimpleMiddleware
from data.loader import bot, db
import handlers
db.create_users_table()
# from parser_file import OpenShopParser

# from middlewares import SimpleMiddleware
# from data.loader import bot, db


# import handlers


bot.setup_middleware(SimpleMiddleware(1)) # bu botga qayta qayta yozmaslik uchun limit(sekundda) kiritiladi

if __name__ == '__main__':
    bot.infinity_polling()
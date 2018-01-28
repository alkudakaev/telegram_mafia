import telebot
# import cherrypy
import config
import mafia_func


"""
Диалог с пользователем
1) Старт
2) Создать комнату или присоединиться?
3) Ввести/выбрать наименование комнаты
4) Готовы начать игру? 
5) Список игроков
6) В игре Х участников, из них Y - мафия, Z - доктор/любовница
"""
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def first_dialog(message): # Название функции не играет никакой роли, в принципе
    name = message.from_user.first_name
    mafia_func.dialog_keyboard(1)
    bot.send_message(message.chat.id, 'Привет, ' + name + '. Хочешь начать или присоединиться к игре?',
                     reply_markup=mafia_func.dialog_keyboard(1))


@bot.message_handler(func=lambda message: message.text == "Начать")
def start_game(message):
    i = 0
    mafia_func.room_code()
    bot.send_message(message.chat.id, 'Комната для игры создана.'
                                      'Ваш код комнаты:' + mafia_func.room_code(),
                     reply_markup=mafia_func.clean_keyboard())


@bot.message_handler(func=lambda message: message.text == "Присоединиться")
def start_game(message):
    bot.send_message(message.chat.id, 'Введите код комнаты.')


if __name__ == '__main__':
    bot.polling(none_stop=True)


# WEBHOOK_HOST = '139.59.143.83'
# WEBHOOK_PORT = 88  # 443, 80, 88 или 8443 (порт должен быть открыт!)
# WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше
#
# WEBHOOK_SSL_CERT = './webhook_mycert.pem'  # Путь к сертификату
# WEBHOOK_SSL_PRIV = './webhook_mykey.pem'  # Путь к приватному ключу
#
# WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
# WEBHOOK_URL_PATH = "/%s/" % (config.token)
#
# bot = telebot.TeleBot(config.token)
#
#
# class WebhookServer(object):
#     @cherrypy.expose
#     def index(self):
#         if 'content-length' in cherrypy.request.headers and \
#                         'content-type' in cherrypy.request.headers and \
#                         cherrypy.request.headers['content-type'] == 'application/json':
#             length = int(cherrypy.request.headers['content-length'])
#             json_string = cherrypy.request.body.read(length).decode("utf-8")
#             update = telebot.types.Update.de_json(json_string)
#             # Эта функция обеспечивает проверку входящего сообщения
#             bot.process_new_updates([update])
#             return ''
#         else:
#             raise cherrypy.HTTPError(403)
#
#
# # Хэндлер на все текстовые сообщения
# @bot.message_handler(func=lambda message: True, content_types=['text'])
# def echo_message(message):
#     bot.reply_to(message, message.text)
#     bot.send_message(message.chat, message.message_id)
#
#
# # Снимаем вебхук перед повторной установкой (избавляет от некоторых проблем)
# bot.remove_webhook()
#
#
# # Ставим заново вебхук
# bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
#                 certificate=open(WEBHOOK_SSL_CERT, 'r'))
#
# # Указываем настройки сервера CherryPy
# cherrypy.config.update({
#     'server.socket_host': WEBHOOK_LISTEN,
#     'server.socket_port': WEBHOOK_PORT,
#     'server.ssl_module': 'builtin',
#     'server.ssl_certificate': WEBHOOK_SSL_CERT,
#     'server.ssl_private_key': WEBHOOK_SSL_PRIV
# })
#
#  # Собственно, запуск!
# cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})

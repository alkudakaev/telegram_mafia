import requests
import config
import mafia_oop

token = config.token
URL = 'https://api.telegram.org/bot'+token+'/'

"""
Диалог с пользователем
1) Старт
2) Создать комнату или присоединиться?
3) Ввести/выбрать наименование комнаты
4) Готовы начать игру? 


"""






# def get_updates():
#     url = URL + 'getupdates'
#     r = requests.get(url)
#     return r.json()
#
#
# def get_message():
#     data = get_updates()
#     chat_id = data['result'][-1]['message']['chat']['id']
#     message_text = data['result'][-1]['message']['text']
#     message = {'chat_id': chat_id,
#                'text': message_text}
#     return message
#
#
# def send_message(chat_id, text = 'Wait a second...'):
#     url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id,text)
#     requests.get(url)
#
#
#
# def main():
#     answer = get_message()
#     chat_id = answer['chat_id']
#     text = answer['text']
#     if text == '/start':
#         send_message(chat_id,'Сыграем в Мафию?')
#     elif text == '/y':
#         send_message(chat_id, 'Чооо?')
#
#
# if __name__ == '__main__':
#     main()
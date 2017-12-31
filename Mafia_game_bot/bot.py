import requests

import mytoken

token = mytoken.token
URL = 'https://api.telegram.org/bot'+token+'/'


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']
    message = {'chat_id': chat_id,
               'text': message_text}
    return message

def send_message(chat_id, text = 'Wait a second...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id,text)
    requests.get(url)



def main():
    # d = get_updates()
    #
    # with open('updates.json', 'w') as f:
    #     json.dump(d, f, indent=2, ensure_ascii=False)
    #
    # print(get_message())
    answer = get_message()
    chat_id = answer['chat_id']
    send_message(chat_id,'Что ты хочешь на ужин?')

if __name__ == '__main__':
    main()
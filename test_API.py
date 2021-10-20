import requests

API_link = 'https://api.telegram.org/bot1818382742:AAEghP39AeLNzpIJRhUZyZhA1Z9wFLR2OU8'

if __name__ == '__main__':
    updates = requests.get(API_link + '/getUpdates?offset=-1').json()
    print(updates, '\n')

    message = updates['result'][0]['message']
    print(message, '\n')

    chat_id = message['from']['id']
    text = message['text']
    print(chat_id, text, '\n')

    sent_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text={text}")
    print(sent_message.text)
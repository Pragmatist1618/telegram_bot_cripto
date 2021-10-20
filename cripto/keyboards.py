from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

test = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Hi')
            ],
            [
                KeyboardButton(text='One'),
                KeyboardButton(text='Two')
            ],
        ],
        resize_keyboard=True
    )

menu_kb = InlineKeyboardMarkup(row_width=2)
menu_btn_1 = InlineKeyboardButton('Binance', callback_data='binance')
menu_btn_2 = InlineKeyboardButton('Metamask', callback_data='metamask')
menu_btn_3 = InlineKeyboardButton('Настройки API', callback_data='api')
menu_btn_4 = InlineKeyboardButton('Статус', callback_data='state')
menu_btn_5 = InlineKeyboardButton('Продлить подписку', callback_data='pay')
menu_btn_6 = InlineKeyboardButton('Информация', callback_data='info')
menu_btn_7 = InlineKeyboardButton('Поддержка', callback_data='support')
menu_kb.add(menu_btn_1)
menu_kb.add(menu_btn_2)
menu_kb.row(menu_btn_3, menu_btn_4)
menu_kb.add(menu_btn_5)
menu_kb.row(menu_btn_6, menu_btn_7)

api_kb = InlineKeyboardMarkup(row_width=2)
api_btn_1 = InlineKeyboardButton('Удалить API', callback_data='delete_binance_api')
api_btn_2 = InlineKeyboardButton('Инструкция', callback_data='manual_api')
api_btn_3 = InlineKeyboardButton('Меню', callback_data='menu')
api_kb.add(api_btn_1, api_btn_2)
api_kb.add(api_btn_3)

btn_menu = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Меню', callback_data='menu'))

from cripto.app import bot, dp
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove, CallbackQuery, PreCheckoutQuery, ContentType
from cripto.settings import admin_id, PAY_IMAGE_URL, PAYMENTS_TOKEN, SUBSCRIBE_PRICE
from aiogram.dispatcher.filters import Command, Text
import cripto.db as db
import cripto.keyboards as kb
import cripto.messages as msg
from aiogram.utils.markdown import text
from cripto.tools import is_valid_binance_api


async def send_start_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='bot started')


async def send_shutdown_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='bot shutdown')


@dp.message_handler(Command('start'))
async def start_command(message: Message):
    user_id = message.chat.id
    if message.chat.first_name and message.chat.last_name:
        user_name = message.chat.first_name+' '+message.chat.last_name
    elif message.chat.first_name:
        user_name = message.chat.first_name

    db.add_user(user_id=user_id, user_name=user_name, referral_id=None)

    await message.answer(msg.MESSAGES['start'] % user_name + '\n\n' + msg.MESSAGES['menu'],
                         reply_markup=kb.menu_kb)


@dp.message_handler(Command('stop'))
async def stop_command(message: Message):
    pass


@dp.message_handler(Command('help'))
async def help_command(message: Message):
    await message.answer(msg.MESSAGES['help'])


@dp.message_handler(Command('info'))
async def info_command(message: Message):
    await message.answer(msg.MESSAGES['info'])


@dp.message_handler(Command('menu'))
async def menu_command(message: Message):
    menu_kb = kb.menu_kb
    menu_msg = msg.MESSAGES['menu']
    await message.answer(menu_msg,
                         reply_markup=menu_kb)


# test
# @dp.message_handler(Text(equals=['Hi', 'One', 'Two']))
# async def get_menu_answer(message: Message):
#     menu_msg = msg.MESSAGES['menu']
#     await message.answer(f"{menu_msg}: {message.text}",
#                          reply_markup=ReplyKeyboardRemove())


@dp.callback_query_handler(lambda c: c.data)
async def process_callback_kb1btn1(callback_query: CallbackQuery):
    is_pay = False
    keyboard = None

    def binance():
        return 'binance'

    def metamask():
        return 'На текущее время функция недоступна.'

    def api():
        nonlocal keyboard
        keyboard = kb.api_kb

        user_id = callback_query.message.chat.id
        binance_api = db.get_binance_api_or_false(user_id=user_id)

        txt = ''

        if binance_api:
            txt += f"\n <b>API Binance:</b> {binance_api} \n"

        return msg.MESSAGES['api'] % txt

    def info():
        nonlocal keyboard
        keyboard = kb.btn_menu

        return msg.MESSAGES['help']

    def pay():
        nonlocal is_pay
        is_pay = True

        nonlocal keyboard
        keyboard = kb.btn_menu

        return msg.MESSAGES['pay_test']

    def state():
        user_id = callback_query.message.chat.id

        status, date, binance_api, binance_secret_key, metamask_api = db.check_status(user_id)

        if binance_api:
            if is_valid_binance_api(binance_api, binance_secret_key):
                binance_api_msg = msg.MESSAGES['binance_api'] % ('✅', 'подключен')
            else:
                binance_api_msg = msg.MESSAGES['binance_api'] % ('❌', 'данные некорректны')
        else:
            binance_api_msg = msg.MESSAGES['binance_api'] % ('❌', 'не подключен')

        if status:
            status_msg = msg.MESSAGES['status_true'] % date
        else:
            status_msg = msg.MESSAGES['status_false']

        return text(status_msg, binance_api_msg, sep='\n')

    def support():
        nonlocal keyboard
        keyboard = kb.btn_menu

        return msg.MESSAGES['info']

    def delete_binance_api():
        user_id = callback_query.message.chat.id

        db.delete_binance_api(user_id)

        return msg.MESSAGES['delete_binance_api']

    def manual_api():
        return msg.MESSAGES['manual_api']

    def menu():
        nonlocal keyboard
        keyboard = kb.menu_kb

        return msg.MESSAGES['menu']

    switcher = {
        'binance': binance,
        'metamask': metamask,
        'api': api,
        'info': info,
        'pay': pay,
        'state': state,
        'support': support,
        'delete_binance_api': delete_binance_api,
        'manual_api': manual_api,
        'menu': menu
    }

    func_name = callback_query.data

    txt = switcher.get(func_name, 'nothing')()

    if is_pay:
        await bot.send_invoice(
            callback_query.message.chat.id,
            title=msg.MESSAGES['pay_title'],
            description=msg.MESSAGES['pay_description'],
            provider_token=PAYMENTS_TOKEN,
            currency='rub',
            photo_url=PAY_IMAGE_URL,
            photo_height=512,  # !=0/None, иначе изображение не покажется
            photo_width=512,
            photo_size=512,
            is_flexible=False,  # True если конечная цена зависит от способа доставки
            prices=[SUBSCRIBE_PRICE],
            start_parameter='pay_subscribe',
            payload='payload'
        )

    await callback_query.message.answer(text=txt,
                                        reply_markup=keyboard)


@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: Message):
    user_id = message.chat.id

    db.renew_subscription_for_user(user_id)

    print('successful_payment:')
    pmnt = message.successful_payment.to_python()
    for key, val in pmnt.items():
        print(f'{key} = {val}')

    await bot.send_message(
        message.chat.id,
        msg.MESSAGES['successful_payment']
    )


@dp.message_handler(regexp=r'^api binance \*.+\*.+\*$')
async def add_binance_api(message: Message):
    user_id = message.chat.id
    binance_api = message.text.split('*')[1]
    binance_secret_key = message.text.split('*')[2]

    db.add_binance_api(user_id=user_id, api=binance_api, secret_key=binance_secret_key)

    await message.answer(msg.MESSAGES['add_binance_api'], reply_markup=kb.btn_menu)


@dp.message_handler()
async def echo(message: Message):
    txt = message.text
    print(message.chat.first_name, message.text)
    await message.answer(text=txt)

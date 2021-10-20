from aiogram.utils.markdown import text

start_msg = '<b>Добро пожаловать, %s!</b>'
menu_msg = 'Вспользуйтесь меню для совершения действий или ожидайте информацию от робота.'

info_msg = text(
    '<b>Справочная информация</b>\n',
    '*' * 30 + '\n',
    'Telegram канал Criptus: https://cutt.ly/hvtmj1q',
    'YouTube канал Criptus: https://www.youtube.com/channel/UCGzOtu1tlrOeq_-jXzV-Fng\n',
    '*' * 30 + '\n',
    'При возникновении неполадок, неисправностей, предложений и пожеланий: @redwh1te76\n',
    '*' * 30 + '\n',
    sep='\n'
)

help_msg = text(
    'Доступные команды:\n',
    '/start - приветствие',
    '/menu - меню',
    '/info - информация',
    sep="\n"
)

status_true_msg = 'Ваша подписка действительна до: <b>%s</b>'

status_false_msg = 'Подписка закончилась. 🤷‍♂ Но Вы легко можете ее продлить!'

pay_test_msg = text(
    'Для оплаты используйте данные тестовой карты:',
    '<b>1111 1111 1111 1026</b>,',
    '<b>12/22</b>, CVC <b>000</b>.',
    sep='\n'
)

pay_title_msg = 'Спасибо, что выбрали нашего бота.'

pay_description_msg = 'После оплаты функционал бота будет доступен в течении месяца, ' \
                      'более подробную информацию можно посмотреть в меню. \n' \
                      'При повторной оплате подписка продлится еще на месяц.'

successful_payment_msg = 'Ура! Платеж совершен успешно! Приятного пользования ботом!'

binance_api_msg = '%s <b>Binance API:</b> %s'

api_msg = text(
    'Центр управлением API:',
    '%s',
    sep='\n'
)

delete_binance_api_msg = 'API удален.'

add_binance_api_msg = 'API успешно добавлен.'

manual_api_msg = text(
    '<b>Подключение API:</b>',
    'Для добавления API необходимо отправить сообщением Ваш ключ API и секретный ключ в формате:\n',
    '<b>api binance *API*Секрутный ключ*</b>\n',
    'например:\n',
    '<b>api binance *HIO23yhjkn213FUIsdw095Hjkb*Jnbsdi324d08skGYGHd*</b>',
    '\n<b>Настоятельно рекомендуется, при создании API, в настройках указать - только для чтения!!!</b>',
    sep='\n'
)

MESSAGES = {
    'start': start_msg,
    'menu': menu_msg,
    'help': help_msg,
    'info': info_msg,
    'status_true': status_true_msg,
    'status_false': status_false_msg,
    'pay_test': pay_test_msg,
    'pay_title': pay_title_msg,
    'pay_description': pay_description_msg,
    'successful_payment': successful_payment_msg,
    'binance_api': binance_api_msg,
    'api': api_msg,
    'delete_binance_api': delete_binance_api_msg,
    'add_binance_api': add_binance_api_msg,
    'manual_api': manual_api_msg,
}

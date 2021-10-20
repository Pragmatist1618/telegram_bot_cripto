from datetime import datetime
from math import ceil, trunc, floor
import requests
from cripto.tools import create_sha256_signature
from cripto.settings import BINANCE_API_TEST, BINANCE_KEY_TEST


def account_status(api, key):
    url = 'https://binance.com/wapi/v3/accountStatus.html'

    headers = {"X-MBX-APIKEY": api,
               "Content-Type": "application/x-www-form-urlencoded"}

    timestamp = str(floor(datetime.now().timestamp() * 1000))
    sign = create_sha256_signature(key=key, message='timestamp=' + timestamp)

    data = {'timestamp': timestamp,
            'signature': sign}

    response = requests.get(url, headers=headers, params=data).json()

    # {'msg': 'Invalid Api-Key ID.'}
    # {'msg': 'Normal', 'success': True}
    if response['msg'] == 'Normal':
        return True
    else:
        return False


if __name__ == '__main__':
    print(account_status(api=BINANCE_API_TEST, key=BINANCE_KEY_TEST))

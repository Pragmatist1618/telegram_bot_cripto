import sqlite3, datetime

connect = sqlite3.connect('users.db')
cursor = connect.cursor()


def create_db():
    create_table_query = ("""
        CREATE TABLE IF NOT EXISTS users(
            id                  INTEGER     NOT NULL    PRIMARY KEY     AUTOINCREMENT,
            user_id             INTEGER     NOT NULL    UNIQUE,
            user_name           TEXT        NOT NULL,
            status              INTEGER     NOT NULL    DEFAULT 1,
            referral_id         INTEGER,     
            joining_date        timestamp,
            subscription_date   timestamp,
            binance_api         TEXT,
            binance_secret_key  TEXT,
            metamask_api        TEXT,
        )
    """)

    cursor.execute(create_table_query)
    connect.commit()


def test_add_user():
    # user_test = [1, 191707625, 'Артём', 1, 1]
    # cursor.execute("INSERT INTO users VALUES(?,?,?,?,?);", user_test)

    joining_date = datetime.datetime.now()
    data_tuple = (191707625, 'Artyom', 'NULL', joining_date)

    sqlite_insert_query = """INSERT INTO users
                              (user_id, user_name, referral_id, joining_date)
                              VALUES
                              (?, ?, ?, ?);"""

    cursor.execute(sqlite_insert_query, data_tuple)
    connect.commit()


def print_all_items():
    cursor.execute("SELECT * FROM users")
    all_results = cursor.fetchall()
    print(all_results)


def delete_db():
    cursor.execute("DROP TABLE users")
    connect.commit()


def add_user(user_id, user_name, referral_id=None):
    joining_date = datetime.datetime.now()
    data_tuple = (user_id, user_name, referral_id, joining_date)

    sqlite_select_query = f"SELECT user_id, status FROM users WHERE user_id = {user_id}"
    cursor.execute(sqlite_select_query)
    data = cursor.fetchone()

    if data is None:
        sqlite_insert_query = """INSERT INTO users
                                      (user_id, user_name, referral_id, joining_date)
                                      VALUES
                                      (?, ?, ?, ?);"""

        cursor.execute(sqlite_insert_query, data_tuple)
        connect.commit()
    elif data and data[1] == 0:
        sqlite_update_query = f"UPDATE users SET status = 1 WHERE user_id = {user_id}"

        cursor.execute(sqlite_update_query)
        connect.commit()


def check_status(user_id):
    sqlite_select_query = f"SELECT subscription_date, binance_api, binance_secret_key, metamask_api " \
                          f"FROM users WHERE user_id = {user_id}"

    cursor.execute(sqlite_select_query)
    data = cursor.fetchone()

    current_time = datetime.datetime.now()
    subscription_date = data[0]

    binance_api = data[1]
    binance_secret_key = data[2]
    metamask_api = data[3]

    if subscription_date:
        subscription_date = datetime.datetime.strptime(subscription_date, '%Y-%m-%d %H:%M:%S.%f')

    if subscription_date:
        status = subscription_date > current_time
    else:
        status = False

    if subscription_date:
        subscription_date_str = subscription_date.strftime('%Y-%m-%d %H:%M:%S')
    else:
        subscription_date_str = None

    return status, subscription_date_str, binance_api, binance_secret_key, metamask_api


# def renew_subscription_for_everyone(days):
#     current_time = datetime.datetime.now()
#
#     sqlite_update_query = f"UPDATE users SET status = 1 WHERE user_id = {user_id}"
#
#     cursor.execute(sqlite_update_query)
    # connect.commit()


def renew_subscription_for_user(user_id):
    from dateutil.relativedelta import relativedelta

    current_time = datetime.datetime.now()

    date_after_month = current_time + relativedelta(months=1)

    sqlite_update_query = f"UPDATE users SET subscription_date = (?) WHERE user_id = {user_id}"

    cursor.execute(sqlite_update_query, (date_after_month, ))
    connect.commit()


def delete_binance_api(user_id):
    sqlite_update_query = f"UPDATE users SET binance_api = NULL, binance_secret_key = NULL " \
                          f"WHERE user_id = {user_id}"

    cursor.execute(sqlite_update_query)
    connect.commit()


def add_binance_api(user_id, api, secret_key):
    sqlite_update_query = f"UPDATE users SET binance_api = ?, binance_secret_key = ? " \
                          f"WHERE user_id = {user_id}"

    cursor.execute(sqlite_update_query, (api, secret_key, ))
    connect.commit()


def get_binance_api_or_false(user_id):
    sqlite_select_query = f"SELECT binance_api FROM users WHERE user_id = {user_id}"

    cursor.execute(sqlite_select_query)
    data = cursor.fetchone()

    binance_api = data[0]

    if binance_api:
        return binance_api
    else:
        return False


if __name__ == '__main__':
    # create_db()

    # test_add_user()

    print_all_items()

    # delete_db()

    # renew_subscription_for_user(1252089809)

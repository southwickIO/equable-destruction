import os
import sqlite3

def check_cookies(browser):
    if browser == 'chrome':
        cookie_file = os.path.expanduser('~/.config/google-chrome/Default/Cookies')
    elif browser == 'firefox':
        cookie_file = os.path.expanduser('~/.mozilla/firefox/*.default/cookies.sqlite')
    else:
        raise Exception('Invalid browser name')

    conn = sqlite3.connect(cookie_file)
    c = conn.cursor()
    c.execute('SELECT host_key, name, value, path, expires_utc FROM cookies')
    print('[*] HTTP Cookies for %s:' % browser)
    for row in c.fetchall():
        host_key, name, value, path, expires_utc = row
        print('  Host Key: %s' % host_key)
        print('  Name: %s' % name)
        print('  Value: %s' % value)
        print('  Path: %s' % path)
        print('  Expires UTC: %s' % expires_utc)

check_cookies('chrome')
check_cookies('firefox')
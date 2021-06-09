# pip install selenium, pyautogui, opencv, pillow
# seleniumを動かすには、webdriverが必要。https://github.com/mozilla/geckodriver/releases
#からダウンロードして、exeファイルを任意のフォルダに保存。右フォルダにPATHを通す。
#あと、Firefoxをインストールしておく必要あり。

import os
import time
import pyautogui
from selenium.webdriver import Firefox

#ブラウザの起動
driver = Firefox()
driver.get("https://twitter.com/login")

# ログイン画面まで待機 画像は適宜変更が必要な場合あり。
while pyautogui.locateOnScreen('login.png' , confidence = 0.8) = False
    time.sleep(1)

#ログインIDを入力
pyautogui.write("自分のID")

#パスワードを入力
pyautogui.press("tab")
pyautogui.write("自分のパスワード")

#ログインボタンをクリック
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(5)

#ツイートボタン1をクリック
position = pyautogui.locateOnScreen('tweet1.png' , confidence = 0.8)
pyautogui.click(position)

time.sleep(3)

#文字を入力。日本語入力不可なので、日本語入力したい場合、コピペする。
pyautogui.write("Hello World")
#pyautogui.hotkey('ctrl', 'v')で貼り付け。

time.sleep(1)

#ツイートボタン2をクリック
position = pyautogui.locateOnScreen('tweet2.png' , confidence = 0.8)
pyautogui.click(position)

time.sleep(2)

driver.quit()

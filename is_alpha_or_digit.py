# 入力した文字がアルファベットか数字かを判定するプログラム
character = input("文字を入力してください: ")

if character.isalpha():
    print("入力された文字はアルファベットです。")
elif character.isdigit():
    print("入力された文字は数字です。")
else:
    print("入力された文字はアルファベットでも数字でもありません。")

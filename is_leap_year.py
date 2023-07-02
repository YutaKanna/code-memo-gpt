# 閏年（うるうどし）の判定をするプログラム
def is_leap_year(year):
    """
    引数として与えられた年が閏年かどうかを判定する関数です。
    閏年の場合はTrue、閏年でない場合はFalseを返します。
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

# テスト
year = int(input("年を入力してください: "))
if is_leap_year(year):
    print(year, "年は閏年です")
else:
    print(year, "年は閏年ではありません")

def find_max_number(num1, num2, num3):
    max_num = max(num1, num2, num3)
    return max_num

# 3つの数値を入力
input1 = float(input("1つ目の数値を入力してください: "))
input2 = float(input("2つ目の数値を入力してください: "))
input3 = float(input("3つ目の数値を入力してください: "))

# 関数を呼び出して結果を表示
max_number = find_max_number(input1, input2, input3)
print("一番大きい数値は", max_number, "です。")

def check_even_odd(num):
    if num % 2 == 0:
        return "偶数です"
    else:
        return "奇数です"

# ユーザーからの入力を受け取る
num = int(input("整数を入力してください: "))

result = check_even_odd(num)
print(result)

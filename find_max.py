def find_max(numbers):
    if not numbers:  # リストが空の場合
        return None

    max_num = numbers[0]  # 最初の数を仮の最大値とする

    for num in numbers:
        if num > max_num:  # より大きな数が見つかった場合
            max_num = num  # 最大値を更新

    return max_num

# nの値を入力
n = int(input("整数の個数を入力してください: "))

numbers = []
for i in range(n):
    num = int(input(f"整数{i+1}を入力してください: "))
    numbers.append(num)

max_number = find_max(numbers)
print("最大値:", max_number)

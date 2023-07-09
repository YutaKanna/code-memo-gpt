def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_number = 8

result = binary_search(numbers, target_number)
if result != -1:
    print("要素はインデックス", result, "にあります。")
else:
    print("要素は見つかりませんでした。")

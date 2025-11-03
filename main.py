def bubble_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if reverse:
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print("Введите числа через пробел:")
numbers = list(map(int, input().split()))
direction = input("Введите направление сортировки (возрастание/убывание): ").lower()
reverse_sort = direction == "убывание"
sorted_numbers = bubble_sort(numbers.copy(), reverse_sort)
direction_text = "по убыванию" if reverse_sort else "по возрастанию"
print(f"Отсортированные числа {direction_text}: {sorted_numbers}")
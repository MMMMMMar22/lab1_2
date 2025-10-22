def bubble_sort_ascending(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers = list(map(int, input("Введите числа через пробел: ").split()))
sorted_numbers = bubble_sort_ascending(numbers)
print("Отсортировано по возрастанию:", sorted_numbers)
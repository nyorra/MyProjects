def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def shaker_sort(data):
    n = len(data)
    left = 0
    right = n - 1
    while left < right:
        for i in range(left, right):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        right -= 1
        for i in range(right, left, -1):
            if data[i] < data[i - 1]:
                data[i], data[i - 1] = data[i - 1], data[i]
        left += 1
    return data

def combination_sort(data):
    def get_next_gap(current_gap):
        current_gap = (current_gap * 10) // 13
        return max(current_gap, 1)

    gap = len(data)
    swapped = True

    while gap > 1 or swapped:
        gap = get_next_gap(gap)
        swapped = False
        for i in range(len(data) - gap):
            if data[i] > data[i + gap]:
                data[i], data[i + gap] = data[i + gap], data[i]
                swapped = True
    return data


def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

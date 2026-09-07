def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    return numbers

print(bubble_sort([2, 4, 6, 7, 3, 3, 20]))
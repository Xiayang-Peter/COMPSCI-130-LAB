def binary_search(numbers,item):
    if numbers == []:
        return False
    
    if numbers[len(numbers) // 2] == item:
        print(f"{numbers[0:(len(numbers) // 2)]} {item} {numbers[(len(numbers) // 2) + 1:]}")
        return True
    
    elif numbers[len(numbers) // 2] > item:
        print(f"{numbers[0:(len(numbers) // 2)]} {numbers[len(numbers) // 2]} {numbers[(len(numbers) // 2) + 1:]}")
        return binary_search(numbers[0:(len(numbers) // 2)], item)
    
    elif numbers[len(numbers) // 2] < item:
        print(f"{numbers[0:(len(numbers) // 2)]} {numbers[len(numbers) // 2]} {numbers[(len(numbers) // 2) + 1:]}")
        return binary_search(numbers[(len(numbers) // 2) + 1:], item)

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))
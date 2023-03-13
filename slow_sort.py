import time

def slow_sort(numbers: list) -> None:
    size = len(numbers)
    sorted_array = [-1_000_001] * size
    last_iter_removed = False
    while True:
        # Find the minimum number in the list
        min_number = 1_000_001
        for number in numbers:
            if number < min_number:
                min_number = number
        
        # Check if the minimum number is already in the sorted array
        already_sorted = False
        for sorted_number in sorted_array:
            if sorted_number == min_number and not last_iter_removed:
                already_sorted = True
                last_iter_removed = True
        
        # find the index of the minimum number in the original array
        found_index = 1_000_001
        if already_sorted:
            for i in range(size):
                if numbers[i] == min_number and found_index == 1_000_001:
                    found_index = i

        # Remove the minimum number from the original array, if it is already in the sorted array
        for i in range(size - 1):
            if i >= found_index:
                numbers[i] = numbers[i + 1]
        
        placed = False

        # Clear the last element of the original array, if a number was removed
        if found_index != 1_000_001:
            numbers[size - 1] = 1_000_001
            placed = True    
        
        # Place the minimum number in the sorted array, if it is not already in the sorted array
        for i in range(size):
            if sorted_array[i] == -1_000_001 and not placed:
                sorted_array[i] = min_number
                placed = True
                last_iter_removed = False
        
        # stop the loop if the original array is empty
        if numbers[0] == 1_000_001:
            # print('done')
            break
                    
                
        # sorted_array.append(min_number)
    
    numbers.clear()
    numbers.extend(sorted_array)

    

def main() -> None:
    # input_file = open('numbers50.txt', 'r')
    
    # input = input_file.readline
    
    size = int(input())
    numbers = [0] * size
    
    for i in range(size):
        numbers[i] = int(input())
    
    slow_sort(numbers)

    with open(f'output{size}.txt', 'w') as file:
        for number in numbers:
            file.write(f'{number}\n')

if __name__ == '__main__':
    start_time = time.time_ns() / 1000000
    main()
    end_time = time.time_ns() / 1000000
    
    print(f'Elapsed time: {end_time - start_time} milliseconds.')

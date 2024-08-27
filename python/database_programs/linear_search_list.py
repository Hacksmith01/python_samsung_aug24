import time

sorted_list = list(range(1, 10000000000000000000010000))

def linear_search(lst, target):
    for index, element in enumerate(lst):
        if element == target:
            return index
    return -1

a = 10000000000000000000000

# Start the timer
start_time = time.time()

index = linear_search(sorted_list, a)

# End the timer
end_time = time.time()

if index != -1:
    print(f"Element {a} found at index {index}.")
else:
    print(f"Element {a} not found in the list.")

# Print the elapsed time
print(f"Time taken: {end_time - start_time:.6f} seconds.")

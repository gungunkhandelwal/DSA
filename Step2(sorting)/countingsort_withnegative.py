def counting_sort_with_negatives(arr):
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements

    # Count occurrences
    for num in arr:
        count[num - min_val] += 1

    # Build output array
    output = []
    for i in range(len(count)):
        output.extend([i + min_val] * count[i])

    return output

A = [-3, -1, -2, 0, 2, 1, -3]
print(counting_sort_with_negatives(A)) 

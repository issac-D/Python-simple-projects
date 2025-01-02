def non_coalescing_example(input_list):
    result = []
    for i in range(len(input_list)):
        # Check if the current element is the same as the previous element
        if i == 0 or input_list[i] != input_list[i-1]:
            result.append(input_list[i])
    return result

# Example usage
input_data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 1, 2, 2]
output_data = non_coalescing_example(input_data)
print("Original list:", input_data)
print("Non-coalesced list:", output_data)

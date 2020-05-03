def rearrange_digits(input_list):

	def merge(left, right):
		left_index = 0
		right_index = 0

		merged = []

		while left_index < len(left) and right_index < len(right):
			if left[left_index] < right[right_index]:
				merged.append(left[left_index])
				left_index += 1
			else:
				merged.append(right[right_index])
				right_index += 1

		for remaining in left[left_index:]:
			merged.append(remaining)

		for remaining in right[right_index:]:
			merged.append(remaining)

		return merged
    
	def merge_sort(array):

		if len(array) <= 1:
			return array
	
		left = array[0:(len(array) // 2)]
		right = array[(len(array) // 2):]

		left = merge_sort(left)
		right = merge_sort(right)

		return merge(left, right)

	def max_pair(sorted):
		pair_1 = ""
		pair_2 = ""

		for i in range(len(sorted) - 1, -1, -2):
			pair_1 += str(sorted[i])
		
		for i in range(len(sorted) - 2, -1, -2):
			pair_2 += str(sorted[i])

		return [int(pair_1), int(pair_2)]
	
	sorted = merge_sort(input_list)

	return max_pair(sorted)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
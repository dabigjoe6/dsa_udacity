def rotated_array_search(input_list, number):
	
	def search(nums, target):
		
		if len(nums) <= 0:
			return -1
		
		def find_pivot(start, end):
			mid = (start + end) // 2
			
			if nums[mid] > nums[mid + 1]:
				return mid + 1
			else:
				if nums[start] > nums[mid]:
					return find_pivot(start, mid - 1)
				else:
					return find_pivot(mid + 1, end)
				
		
		def binary_search(start, end):
			mid = (start + end) // 2
			
			if start > end:
				return -1
			
			if nums[mid] == target:
				return mid
			
			if start == end:
				return -1
			
			if nums[mid] > target:
				return binary_search(start, mid - 1)
			elif nums[mid] < target:
				return binary_search(mid + 1, end)
		
		start = 0
		end = len(nums) - 1
		
		if target == nums[start]:
			return start
		if target == nums[end]:
			return end
		if start == end:
			return -1
		
		
		if nums[start] < nums[end]:
			return binary_search(start, end)
		else:
			pivot = find_pivot(start, end)
			
			if nums[pivot] == target:
				return pivot
			
			if target > nums[pivot] and target < nums[end]:
				return binary_search(pivot, end)
			else:
				return binary_search(start, pivot)

	return search(input_list, number)
	
def linear_search(input_list, number):
	for index, element in enumerate(input_list):
		if element == number:
			return index
	return -1

def test_function(test_case):
	input_list = test_case[0]
	number = test_case[1]
	if linear_search(input_list, number) == rotated_array_search(input_list, number):
		print("Pass")
	else:
		print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
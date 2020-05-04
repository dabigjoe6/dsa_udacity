def get_new_pivot(items, begin_index, end_index):    
	left_index = begin_index
	pivot_index = end_index
	pivot_value = items[pivot_index]

	while (pivot_index != left_index):

		item = items[left_index]

		if item <= pivot_value:
			left_index += 1
			continue

		items[left_index] = items[pivot_index - 1]
		items[pivot_index - 1] = pivot_value
		items[pivot_index] = item
		pivot_index -= 1

	return pivot_index
    
def quicksort(items, begin_index, end_index):
	if end_index <= begin_index:
		return

	pivot_index = get_new_pivot(items, begin_index, end_index)
	quicksort(items, begin_index, pivot_index - 1)
	quicksort(items, pivot_index + 1, end_index)


def sort(nums):
	quicksort(nums, 0, len(nums) - 1)

	print(nums)

sort([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
sort([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
sort([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
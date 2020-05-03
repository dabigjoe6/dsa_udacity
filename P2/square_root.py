def sqrt(number):

	def sqrt_helper(lower_bound, upper_bound):
		if upper_bound == 1 or upper_bound == 0:
			return upper_bound

		if lower_bound > upper_bound:
			return upper_bound

		mid = (upper_bound + lower_bound) // 2

		mid_square = mid * mid

		if mid_square > number:
			return sqrt_helper(lower_bound, mid - 1)
		elif mid_square < number:
			return sqrt_helper(mid + 1, upper_bound)
		elif mid_square == number:
			return mid
    
	return sqrt_helper(0, number)


sqrt(25)

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
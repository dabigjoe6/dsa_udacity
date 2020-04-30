"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

bangalore_calls = {}

bangalore_to_bangalore_count = 0
bangalore_calls_count = 0

codes_of_receiving_numbers = {}


def check_bangalore(outgoing_call, receiving_call):
	global bangalore_calls_count
	global bangalore_to_bangalore_count
	if "(080)" in outgoing_call:
		bangalore_calls[outgoing_call] = receiving_call
		bangalore_calls_count += 1
		if "(080)" in receiving_call:
			bangalore_to_bangalore_count += 1

def get_code(number):
	number.strip()

	if number[0] == "(" and number[1] == "0":
		code = re.search('\(([^)]+)\)', number).group()
		return code
	elif " " in number and (number[0] == "7" or number[0] == "8" or number[0] == "9"):
		code = number[0:4]
		return code
	elif "140" in number:
		return "140"

	return None

with open('texts.csv', 'r') as f:
	reader = csv.reader(f)
	texts = list(reader)

with open('calls.csv', 'r') as f:
	reader = csv.reader(f)
	calls = list(reader)
	for call in calls:
		outgoing_call = call[0]
		receiving_call = call[1]
		check_bangalore(outgoing_call, receiving_call)


for bangalore_call in bangalore_calls:
	# print(bangalore_calls[bangalore_call])
	code = get_code(bangalore_calls[bangalore_call])
	if not code in codes_of_receiving_numbers:
		codes_of_receiving_numbers[code] = ""

def print_codes():
	codes = []
	
	for receiving_code in codes_of_receiving_numbers:
		codes.append(receiving_code)
	
	print("The numbers called by people in Bangalore have codes:")

	codes.sort()

	for code in codes:
		print(code)

def percentage_of_bangalore_calls():
	percentage = bangalore_to_bangalore_count / bangalore_calls_count * 100
	print("%.2f" % percentage + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

print_codes()
print("\n")
percentage_of_bangalore_calls()



"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

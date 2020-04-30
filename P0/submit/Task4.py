"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

sends_texts_numbers = {}
recieve_texts_numbers = {}
receive_calls_numbers = {}

telemarketers_lookup = {}
telemarketers = []

with open('texts.csv', 'r') as f:
		reader = csv.reader(f)
		texts = list(reader)

		for text in texts:
			if not text[0] in sends_texts_numbers:
				sends_texts_numbers[text[0]] = ""
			if not text[1] in recieve_texts_numbers:
				recieve_texts_numbers[text[1]] = ""

with open('calls.csv', 'r') as f:
		reader = csv.reader(f)
		calls = list(reader)

		for call in calls:
			if not call[1] in receive_calls_numbers:
				receive_calls_numbers[call[1]] = ""

		for call in calls:
			if not (call[0] in sends_texts_numbers or call[0] in recieve_texts_numbers or call[0] in receive_calls_numbers):
				if not call[0] in telemarketers_lookup:
					telemarketers_lookup[call[0]] = ""

def print_telemarketers():
	global telemarketers

	for telemarketer in telemarketers_lookup:
		telemarketers.append(telemarketer)
	
	telemarketers.sort()

	print("These numbers could be telemarketers: ")

	for telemarketer in telemarketers:
		print(telemarketer)

print_telemarketers()

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


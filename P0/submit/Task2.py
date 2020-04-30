"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

telephone_numbers = {}

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        if not call[0] in telephone_numbers:
            telephone_numbers[call[0]] = int(call[3])
        else:
            telephone_numbers[call[0]] += int(call[3])

        if not call[1] in telephone_numbers:
            telephone_numbers[call[1]] = int(call[3])
        else:
            telephone_numbers[call[1]] += int(call[3])

longest_time = 0
phone_number = ''

for number in telephone_numbers:
    if telephone_numbers[number] > longest_time:
        longest_time = telephone_numbers[number]
        phone_number = number

print(number + " spent the longest time, " + str(longest_time) +
      " seconds, on the phone during September 2016.")


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

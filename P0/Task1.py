"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

telephone_numbers = {}
number_of_telphone = 0

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    for text in texts:
        if not text[0] in telephone_numbers:
            telephone_numbers[text[0]] = ""
            number_of_telphone += 1

        if not text[1] in telephone_numbers:
            telephone_numbers[text[1]] = ""
            number_of_telphone += 1


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        if not call[0] in telephone_numbers:
            telephone_numbers[call[0]] = ""
            number_of_telphone += 1

        if not call[1] in telephone_numbers:
            telephone_numbers[call[1]] = ""
            number_of_telphone += 1

print("There are " + str(number_of_telphone) +
      " different telephone numbers in the records.")


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

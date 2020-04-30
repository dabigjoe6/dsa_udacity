"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    print("First record of texts, " +
          texts[0][0] + " texts " + texts[0][1] + " at time " + texts[0][2])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    last_record = len(calls) - 1
    print("Last record of calls, " +
          calls[last_record][0] + " calls " + calls[last_record][1] + " at time " + calls[last_record][2] + ", lasting " + calls[last_record][3] + " seconds")


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

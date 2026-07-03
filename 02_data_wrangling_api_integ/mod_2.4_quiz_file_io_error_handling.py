'''
Question 1: File Modes
You open an existing log file using with open("system_log.txt", "w") as file:. What immediately happens to the existing data inside that file, and what mode should you have used if you wanted to keep the old data and add new lines to the bottom?

Question 2: Data Translation
You have a Python dictionary containing a locked hardware resolution: {"res": (1280, 720)}. You write this to a JSON file using json.dump().
Since the JSON format does not natively support Python Tuples, what does that tuple get converted into when it is written to the .json file?

Question 3: Error Flow Tracing
Trace the try/except block below. What is the exact output printed to the terminal?
Python

sensor_data = {"id": "Node_01"}

try:
    print("Initializing...")
    voltage = sensor_data["v_in"]
    print("Voltage captured.")
except KeyError:
    print("Data missing. Using default voltage.")
'''

'''
Answer 1:
Although we only discussed "w" and "r" so I'm not sure if there is an append, in the context of the question, using that 'with open:...' syntax, the json file is immediatly wiped out and replaced with the new data. In order to keep the old data, using "r" for read would be necessary, then a try/except path would work.

Answer 2:
The tuple becomes a json dictionary.

Answer 3:
Data missing. Using default voltage.

'''
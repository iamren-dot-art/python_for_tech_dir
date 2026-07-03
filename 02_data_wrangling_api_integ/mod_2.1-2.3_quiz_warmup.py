'''
Question 1: Mutability & Hardware Constraints (2.1)
You are configuring the I2S audio capture pins for your Embedded Audio/Display Controller. You define them in a tuple: i2s_pins = (18, 19, 20, 21).
Later in the script, you attempt to run i2s_pins.append(22). What exactly does the Python interpreter do, and why is this data structure intentionally chosen for this hardware spec?
    Answer 1: Will return an error (KeyError?) as tupbles are immutable and things like i2s pins don't change, neither should the tupple (or data block containing the information, ie a tuple)

Question 2: Dictionary Error Handling (2.2)
Your IoT Environmental Sensor Network hub receives an MQTT payload from a node:
node_data = {"id": "Sprout_04", "moisture": 45, "battery": 82}

Your script runs the following line to update the UI:
temp_reading = node_data["temperature"]

What exactly happens to your script the moment it hits this line?
    Answer 2: KeyError since there is a new key stated, but no value. The stated key does not exist currently, so cannot be referenced/called.

Question 3: Execution Tracing (2.2)
Trace the following lines of code. What is the exact output printed to the console?

hardware_state = {"protocol": "Bluetooth", "active": True}
default_state = hardware_state

hardware_state["active"] = False

print(default_state["active"])
    Answer 3: True (I think this because the change to 'hardware_state' happened after default state was defined. When it's called)

Question 4: Comprehension Translation (2.3)
Look at the standard for loop below, which filters a list of API response codes to only grab the successful ones (code 200).
Translate this exact logic into a single-line List Comprehension.
raw_codes = [200, 404, 500, 200, 403, 200]
success_codes = []

for code in raw_codes:
    if code == 200:
        success_codes.append(code)

    Answer 4:
    success_codes = [code for code in raw_codes if code == 200]
'''
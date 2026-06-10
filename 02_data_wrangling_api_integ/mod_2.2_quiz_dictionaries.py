'''
Question 1: Data Architecture
When you send a configuration payload to your Local AI Server, why is it mandatory to structure that payload as a Dictionary (Key-Value pairs) rather than a List?
    Answer: Lists are good for parsing data sequentially, but when you need to literally 'look-up' and/or change values. Relying on the list's index value is a dangerous way.

Question 2: Execution Tracing
Trace the following code line-by-line. What is the exact output printed to the console?
Python

node_config = {"id": "Sensor_01", "active": True}
node_config["active"] = False
node_config["battery"] = 85

print(node_config["active"])

    Answer: {'id': 'Sensor_01', 'active': False, 'battery': 85}

Question 3: Error Handling Mechanics
In your Embedded Audio/Display Controller, you have a dictionary storing UI settings. What happens if the interpreter executes print(ui_settings["contrast"]) but the key "contrast" was never actually added to the dictionary?
    Answer: Contrast get's added to the end of the dict
'''
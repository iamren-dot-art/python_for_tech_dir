'''
Your Task:

1. Define your incoming payload list:
    raw_sensors = [45.2, -1.0, 60.5, 33.0, -1.0, 78.1]

2. Write a single list comprehension that creates a new list called clean_sensors. 

3. The comprehension must do two things:
    Filter: Only include the sensor value if it is strictly greater than 0.
    Process: Multiply the valid sensor values by 1.1 (a 10% boost).
4. print() the new clean_sensors list.
'''

raw_sensors = [45.2, -1.0, 60.5, 33.0, -1.0, 78.1]

'''
# IF loop
clean_sensors = []
for level in raw_sensors:
    if level > 0:
        clean_sensors.append(level * 1.1)
'''

clean_sensors = [level * 1.1 for level in raw_sensors if level > 0]

print(clean_sensors)


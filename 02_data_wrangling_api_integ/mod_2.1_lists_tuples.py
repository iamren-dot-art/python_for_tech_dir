"""
Your Task:
- Create a Tuple named sauron_res containing the integer resolution of the Logitech C615 camera: 1280 and 720. Print it.
- Create a List named capture_buffer containing four float values representing recorded file sizes in MB: 45.6, 44.2, 45.0, 44.8.
- Sauron just finished recording a new chunk. Use the .append() method to add a new file size of 45.1 to the end of your capture_buffer list.
- Using Positive Indexing, extract and print the oldest file in the buffer (the very first item).
- Using Negative Indexing, extract and print the newest file in the buffer (the very last item, which you just appended).
"""

sauron_res = (1280, 720)
print(f"Sauron Resolution: {sauron_res}")

capture_buffer = [45.6, 44.2, 45.0, 44.8]
capture_buffer.append(45.1)
print(f"Capture buffer positive index oldest: {capture_buffer[0]}")
print(f"Capture buffer negative index newest: {capture_buffer[-1]}")
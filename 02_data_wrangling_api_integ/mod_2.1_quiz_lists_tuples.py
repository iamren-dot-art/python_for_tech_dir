'''
Question 1: You are writing a Python script to control the 1.3" OLED display on your shortKing hardware. You need to store the screen resolution (128x64). Why is it architecturally better to store this as a Tuple (128, 64) rather than a List [128, 64]?
    Answer: Tuples are unchangable and therefore highly memory efficient. Lists can be appended and modified, but a screen resolution is fixed and modifications may bring down the whole display.

Question 2:
Trace the following execution. What is the exact output printed to the console?

recent_files = ["vid_01.mp4", "vid_02.mp4", "vid_03.mp4", "vid_04.mp4"]
print(recent_files[-3])
    Answer: vid_02.mp4
'''
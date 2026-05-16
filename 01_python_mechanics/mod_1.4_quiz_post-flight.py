"""
Question 1:
You write a function to calculate the aspect ratio of a TouchDesigner output window. Inside the function, you write result = width / height and then print(result). If you try to use this function to dynamically drive the resolution of a Render TOP in another part of your script, what will happen and why?

A:
I'm still learning about TouchDesigner so my frame of reference for analogies using TD concepts is still very limited. That said, I believe since the result of that calculation doesn't go anywhere since there is no return, only print.
"""

"""
Question 2:
Trace the execution of this code line-by-line. What is the exact output printed to the console?

multiplier = 2.0

def scale_vector(x_val):
    multiplier = 5.0
    return x_val * multiplier

final_vector = scale_vector(10)
print(f"Vector: {final_vector} | Global Multiplier: {multiplier}")

A:
Vector: 50 | Global Multiplier: 2.0
"""

"""
Question 3:
You are building an autonomous Python agent (like your planned local Gemma 4 pipeline). You create a variable chat_history = [] inside a function called generate_response(). Every time the function runs, you append the user's prompt to chat_history. Why will this agent suffer from "amnesia" and forget the conversation after every single message?

A:
Since the variable is an empty list, everytime the funtion runs, it creates a new blank list to start from, wiping out any previous input.
"""

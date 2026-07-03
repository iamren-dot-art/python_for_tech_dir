'''
# 🏆 Milestone 1 + 2 Capstone Exam

### This is the crucible. 10 questions testing your absolute retention of everything from environment setup to JSON file I/O. Take your time, trace carefully, and lock in your answers.

### 1. Environment Isolation (Milestone 1.1)
**Q:** You activate your .venv on Oroku_S and install the requests library. If you open a second terminal, do not activate the .venv, and try to run a script that imports requests, what happens and why?

**A:** Python looks for the requests library, but since the .venv isn't active it looks in the user's python folder and fails to find it returning 'ModuleNotFound' error

---

### 2. Assignment vs. Evaluation (Milestone 1.2)
**Q:**
Trace this execution. What is printed?

Python
```python
is_active = False
is_active == True
print(is_active)
```

**A:** False

---

### 3. Control Flow Tracing (Milestone 1.3)
**Q:** Trace this execution line-by-line. What is the exact terminal output?

Python
```python
threshold = 10
levels = [5, 12, 8]

for val in levels:
    if val > threshold:
        print("Clipped")
    else:
        print(val)
```

**A:** 
[Clipped, 12, Clipped]

---

### 4. Scope & Return Mechanics (Milestone 1.4)
**Q:** Why does the print(final_val) statement below result in a crash (NameError), and how would you fix the architecture?

Python
```python
def calculate_scale(width):
    final_val = width * 1.5
    return final_val

calculate_scale(1920)
print(final_val)
```

**A:** 
'final_val' only exists inside the 'calculate_scale()' function and only while the function is running. The current script is looking in the Global Scope for the variable.

---

### 5. Lists vs Tuples (Milestone 2.1)
**Q:** What is the syntactical difference in creating a List versus a Tuple, and what is the primary operational difference (Mutability) between them?

**A:** Lists can be changed, amended, cleared, rewritten. Tuples are permanent, and therefore immutable (unchanging).

---

### 6. Negative Indexing (Milestone 2.1)
**Q:** You have a buffer of recently saved caches:

```caches = ["v01.abc", "v02.abc", "v03.abc", "v04.abc"]```

What exact syntax do you use to target "v03.abc" using negative indexing?

**A:** caches[-1]

---

### 7. Dictionary Mutability & Reading (Milestone 2.2)
**Q:** Trace this execution. What is printed?
Python
```python
config = {"fps": 24, "res": 1080}
config["fps"] = 60
config["render_engine"] = "Redshift"
print(config["fps"])
```

**A:** [Redshift 60]

---

### 8. The Permanence of Mutability (Milestone 2.2)

**Q:** You have a base hardware state: ```default_ui = ["Play", "Stop"]```.
You want to create a working copy to modify without destroying the default state.
Why is active_ui = default_ui dangerous, and what exact syntax must you use instead?

**A:** active_ui = default_ui is dangerous because any changes to the active ui will also affect the default ui. The proposed syntax does not create a new list. It creates a new reference to the same exact object in memory.

```active_ui = default_ui.copy()``` is a shallow copy, ```active_ui = default_ui[:]``` is the pythonic way

--- 

### 9. Comprehension Translation (Milestone 2.3)

**Q:** Translate this standard for loop into a single-line List Comprehension.
Python
```python
raw_volts = [1.2, 5.0, 3.3, 5.0]
safe_volts = []
for v in raw_volts:
    if v < 5.0:
        safe_volts.append(v)
```

**A:** Comprehension
```python
safe_volts = [v for v in raw_volts if v < 5.0 ]
```
---

### 10. File I/O & The with Context (Milestone 2.4)

**Q:** When reading a config.json file, why do we wrap the operation inside a with open(...) as file: block instead of just opening the file manually in a standard variable?

**A:** Python needs to use the json lib to convert json -> python
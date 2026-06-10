# Python for Technical Directors Log

**Primary Architect:** Arian  
**Current Focus:** Python for Technical Directors (v2.0)  
**Objective:** Architecting creative pipelines, bridging 3D design (C4D) with engineering, and building custom toolsets for embedded hardware and autonomous AI agents.

---

## 📅 Project Log & Sabbatical Tracker

### 2026-06-09 | Modules 2.1, 2.2, 2.3: Data Wrangling
* **Pre-Flight Quiz:** Validated architectural choices for hardware constraints (Tuples for locked memory safety vs. Lists for mutable arrays). Corrected execution tracing on dictionary reading vs. writing—specifically identifying that reading a non-existent key causes a fatal `KeyError`, whereas assigning to a non-existent key creates it.
* **Objective:** Manipulate massive data arrays, structure JSON API payloads, and procedurally filter data streams.
* **Actions Completed:**
  * **Lists & Tuples:** Built data buffers for a *Headless Camera Pipeline*, mastering positive (`0`) and negative (`-1`) index targeting. 
  * **Dictionaries:** Constructed the exact JSON Key-Value payload structure required to communicate with the *Local AI Server* (`gemma4:26b`), successfully mutating configuration states on the fly.
  * **Comprehensions:** Processed raw telemetry from the *IoT Environmental Sensor Network*, utilizing a single-line list comprehension to simultaneously filter out error codes (`if level > 0`) and apply a math transformation (`level * 1.1`).
* **Core Concept Hardened:** The Permanence of Mutability. In Python, modifying a list or dictionary alters it permanently in system RAM. To preserve default states (like a hardware factory reset), `.copy()` must be explicitly used to separate the memory references.
* **Status:** Paused at the end of Module 2.3. The Post-Flight Quiz for comprehensions will serve as the Pre-Flight Quiz for the next session.

---

### 2026-05-15 | Module 1.4: Functions & Scope (Milestone 1 Complete)
* **Pre-Flight Quiz:** Validated environment isolation risks (global vs. `.venv`), execution tracing of assignment (`=`) vs. evaluation (`==`), and correct dictionary factory syntax (`{}`).
* **Objective:** Encapsulate logic into reusable functions and manage global/local memory spaces.
* **Actions Completed:**
  * Built `normalize_adc_level()`, a defensive clamping utility for raw hardware sensor data (0-1023 to 0.0-1.0 floats).
  * Hardened the critical distinction between `print()` (diagnostic terminal output) and `return` (actual data payload pipeline delivery).
  * Corrected "ghost operations" by actively assigning math outputs to variables before returning them.
* **Post-Flight Quiz:** 100% accuracy. Flawlessly traced variable shadowing (local overriding global without destroying it) and identified the "amnesia" flaw of initializing state variables inside a local function scope.

---

### 🏁 Milestone 1 Retrospective: Python Mechanics
The structural bedrock is secure. The conceptual leaps from 3D/Compositing pipelines to Python syntax are locked in:
* **Primitives** = Raw parameter data (Strings, Ints, Floats, Bools).
* **Control Flow** = The routing network (If/Else Switch nodes, For/While Timeline loops).
* **Functions** = Custom encapsulated Sub-Systems / Base COMPs with defined Inputs (Arguments) and Outputs (Returns).
* **Scope** = Global Project Settings vs. Temporary Local memory.

**System Readiness:** Cleared to advance to Milestone 2: Data Wrangling & API Integration. The focus shifts from single variables to handling massive data arrays and JSON structures (essential for LLM APIs and procedural scene generation).

### 2026-05-04 | Milestone 1.1: Environment & Git Protocol
* **Objective:** Establish a pristine, reproducible Python environment.
* **Actions Completed:**
  * Initialized Git repository and set up SSH bridge.
  * Generated strict `.gitignore` to prevent tracking bloating the repo with `.venv` or `__pycache__`.
  * Created isolated Python 3.12 virtual environment (`.venv`).
  * Installed core pipeline dependencies (`python-osc`, `pyserial`, `numpy`, `requests`) via `requirements.txt`.
  * Renamed local working directory to include `YYYYMMDD_` prefix for versioned local backups.
* **Notes:** VS Code interpreter successfully locked to the `.venv` path. Ready to begin Python primitives and control flow.

---

## 🛠️ Core Technology Stack
* **Language:** Python 3.12 (Isolated `.venv`)
* **DCC:** Cinema 4D 2026.1.0 
* **Real-Time / Comms:** TouchDesigner, Pyserial, OSC
* **Local AI:** Gemma 4:26b (via Ollama on WSL2 / ROCm 7.2.1)

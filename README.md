# REN: Technical R&D Sabbatical

**Primary Architect:** Arian  
**Current Focus:** Python for Technical Directors (v2.0)  
**Objective:** Architecting creative pipelines, bridging 3D design (C4D) with engineering, and building custom toolsets for embedded hardware and autonomous AI agents.

---

## 📅 Project Log & Sabbatical Tracker

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
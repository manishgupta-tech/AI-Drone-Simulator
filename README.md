# 🚁 AI Drone Simulator

An AI-powered drone simulation system built using **Microsoft AirSim**, featuring autonomous navigation, obstacle avoidance, mission planning, and real-time telemetry.

---

## 📌 Overview

This project simulates an intelligent drone system capable of executing missions in a virtual environment. It integrates AI-based decision-making with real-time control and monitoring using AirSim.

---

## ✨ Features

* 🧭 Autonomous Navigation
* 🚧 Obstacle Avoidance (AI-based)
* 🎯 Mission Planning & Execution
* 📡 Real-time Telemetry System
* 🖥️ Dashboard Visualization (Streamlit)
* 🗄️ Database Integration (PostgreSQL)

---

## 🛠️ Tech Stack

* **Language:** Python
* **Simulation:** Microsoft AirSim
* **Frontend Dashboard:** Streamlit
* **Database:** PostgreSQL
* **Environment:** Virtual Environment (venv)

---

## 📂 Project Structure

```
AirSim_Project/
│── main.py
│── controller.py
│── mission.py
│── obstacle_ai.py
│── telemetry.py
│── db.py
│── dashboard.py
│── config.py
│── requirements.txt
│── README.md
│── venv/ (ignored)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/manishgupta-tech/AI-Drone-Simulator.git
cd AI-Drone-Simulator
```

---

### 2️⃣ Install Python

Make sure Python (3.8+) is installed.

---

### 3️⃣ Setup Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 4️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 5️⃣ Setup AirSim Environment

* Download AirSim environment (Blocks) from Microsoft
* Extract the files

⚠️ **IMPORTANT (Windows Users):**
If the simulator doesn’t run:

👉 Right-click on the `.exe` file → Properties →
👉 Click **"Unblock"** → Apply → OK

---

### 6️⃣ Run the Simulator

* Start the AirSim `.exe` file
* Then run:

```
python main.py
```

---

## ▶️ Usage

* Select mode (e.g., mission / manual)
* Drone executes tasks based on AI logic
* Monitor real-time data via telemetry/dashboard

---

## 📸 Screenshots (Add Yours)

*Add screenshots of your simulation, dashboard, or output here*

---

## 🚀 Future Improvements

* Computer Vision Integration
* Reinforcement Learning-based navigation
* Multi-drone coordination
* Cloud deployment

---

## 👨‍💻 Author

**Manish Gupta**
GitHub: https://github.com/manishgupta-tech

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

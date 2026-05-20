# 🚁 AI Drone Simulator

AI-powered autonomous drone simulation system built using Microsoft AirSim for autonomous navigation, obstacle avoidance, mission planning, and real-time telemetry monitoring.

---

## 📖 Overview

AI Drone Simulator is a simulation platform designed to test and validate intelligent drone behavior in a virtual environment.

The project integrates AI-driven decision-making with real-time drone control and monitoring, allowing safe experimentation before real-world deployment.

---

## ✨ Features

✅ Autonomous Navigation

✅ AI-based Obstacle Avoidance

✅ Mission Planning & Execution

✅ Real-time Telemetry Monitoring

✅ Streamlit Dashboard Visualization

✅ PostgreSQL Integration

✅ Modular Architecture

✅ Scalable System Design

---

## 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Simulation | Microsoft AirSim |
| Dashboard | Streamlit |
| Database | PostgreSQL |
| Environment | Python Virtual Environment |

---

## 📂 Project Structure

```bash
AI-Drone-Simulator/
│
├── main.py
├── controller.py
├── mission.py
├── obstacle_ai.py
├── telemetry.py
├── db.py
├── dashboard.py
├── config.py
├── requirements.txt
├── README.md
└── venv/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/manishgupta-tech/AI-Drone-Simulator.git

cd AI-Drone-Simulator
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🖥 AirSim Setup

1. Download Microsoft AirSim Blocks Environment

2. Extract files

Windows Users:

If simulator fails to launch:

- Right-click `.exe`
- Select **Properties**
- Click **Unblock**
- Apply changes

Launch AirSim before running Python scripts.

---

## ▶ Run Project

Start AirSim environment.

Run:

```bash
python main.py
```

Launch dashboard:

```bash
streamlit run dashboard.py
```

---

## 📊 Workflow

```text
Mission Request
       ↓
AI Navigation
       ↓
Obstacle Detection
       ↓
Telemetry Collection
       ↓
Database Storage
       ↓
Dashboard Monitoring
```

---

## 🚀 Future Improvements

- Computer Vision Integration
- Reinforcement Learning Navigation
- Multi-Drone Coordination
- Cloud Deployment
- Real-time Object Detection
- LLM-powered Mission Commands

---

## 👨‍💻 Author

**Manish Gupta**

GitHub: https://github.com/manishgupta-tech

LinkedIn: https://linkedin.com/in/manishgupta-tech

Portfolio: https://manishgupta-portfolio.vercel.app

---

## ⭐ Support

If you found this project useful, consider giving it a star.

Contributions and suggestions are always welcome.

---

Made with ❤️ by Manish Gupta

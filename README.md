#  AI Drone Simulator

An AI-powered autonomous drone simulation platform built using **Microsoft AirSim**, **Python**, **PostgreSQL**, and **Streamlit**. The system enables intelligent drone navigation, obstacle avoidance, mission execution, and real-time telemetry monitoring in a safe virtual environment.

---

##  Project Overview

The **AI Drone Simulator** is designed to simulate and validate autonomous drone operations before real-world deployment. By integrating AI-driven decision-making with a realistic simulation environment, the platform provides a controlled space for testing navigation algorithms, mission planning strategies, and monitoring systems.

The project follows a modular architecture, making it scalable, maintainable, and suitable for future integration with advanced AI and computer vision capabilities.

---

##  Key Features

### Autonomous Navigation

* Intelligent drone movement and path execution.
* Automated waypoint-based mission traversal.

### AI-Powered Obstacle Avoidance

* Real-time obstacle detection.
* Dynamic route adjustment to avoid collisions.

### Mission Planning & Execution

* Define and execute custom drone missions.
* Support for sequential task management and route optimization.

### Real-Time Telemetry Monitoring

* Track drone position, altitude, velocity, and status.
* Continuous collection of flight metrics.

### Interactive Dashboard

* Built with Streamlit for live visualization.
* Displays mission progress and telemetry data in real time.

### PostgreSQL Integration

* Persistent storage of telemetry and mission logs.
* Supports analytics and historical flight data review.

### Modular & Scalable Architecture

* Decoupled components for navigation, AI, telemetry, and data management.
* Easy to extend with additional AI capabilities.

---

##  System Architecture

```text
Mission Request
       │
       ▼
Mission Planner
       │
       ▼
Drone Controller
       │
       ▼
AI Obstacle Avoidance
       │
       ▼
AirSim Simulation
       │
       ▼
Telemetry Collection
       │
       ▼
PostgreSQL Database
       │
       ▼
Streamlit Dashboard
```

---

##  Technology Stack

| Category               | Technology                                        |
| ---------------------- | ------------------------------------------------- |
| Programming Language   | Python                                            |
| Simulation Environment | Microsoft AirSim                                  |
| Data Visualization     | Streamlit                                         |
| Database               | PostgreSQL                                        |
| Environment Management | Python Virtual Environment                        |
| AI Logic               | Custom Obstacle Avoidance & Navigation Algorithms |

---

##  Project Structure

```bash
AI-Drone-Simulator/
│
├── main.py                # Application entry point
├── controller.py          # Drone control operations
├── mission.py             # Mission planning and execution
├── obstacle_ai.py         # Obstacle detection and avoidance logic
├── telemetry.py           # Flight telemetry collection
├── db.py                  # Database connectivity and operations
├── dashboard.py           # Streamlit monitoring dashboard
├── config.py              # Configuration settings
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── venv/                  # Virtual environment
```

---

##  Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/manishgupta-tech/AI-Drone-Simulator.git

cd AI-Drone-Simulator
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Microsoft AirSim Setup

### Step 1: Download AirSim

Download the AirSim Blocks Environment from Microsoft's AirSim repository.

### Step 2: Launch AirSim

Run the AirSim executable before starting the application.

### Windows Troubleshooting

If the simulator does not launch:

1. Right-click the `.exe` file.
2. Select **Properties**.
3. Click **Unblock**.
4. Apply changes and relaunch.

---

## ▶ Running the Application

### Start AirSim Environment

Launch the AirSim simulation environment.

### Run the Drone Simulator

```bash
python main.py
```

### Launch Monitoring Dashboard

```bash
streamlit run dashboard.py
```

---

##  Workflow

```text
User Mission Request
          │
          ▼
Mission Planning
          │
          ▼
Autonomous Navigation
          │
          ▼
Obstacle Detection & Avoidance
          │
          ▼
Telemetry Collection
          │
          ▼
Database Storage
          │
          ▼
Real-Time Dashboard Monitoring
```

---

##  Future Enhancements

* Computer Vision-based Object Detection
* Reinforcement Learning Navigation Models
* Multi-Drone Fleet Coordination
* Cloud-Based Telemetry Streaming
* Real-Time Video Analytics
* Voice & LLM-Powered Mission Commands
* Geofencing and Flight Safety Controls
* Advanced Route Optimization Algorithms

---

##  Potential Use Cases

* Autonomous Drone Research
* Flight Algorithm Testing
* AI Navigation Experiments
* Mission Planning Validation
* UAV Training Simulations
* Smart Logistics and Surveillance Research

---

##  Author

**Manish Gupta**

* GitHub: https://github.com/manishgupta-tech
* LinkedIn: https://linkedin.com/in/manishgupta-tech
* Portfolio: https://manishgupta-portfolio.vercel.app

---

⭐ If you found this project useful, consider giving it a star on GitHub.

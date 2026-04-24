🔄 Complete Project Workflow & Execution Guide
🧠 1️⃣ System Architecture Overview

This project follows a modular robotics architecture:

User Input → Manual Control → AirSim API → Drone Physics
                    ↓
             Telemetry Logger
               s     ↓
              PostgreSQL Database

The system runs in real-time and uses:

AirSim for simulation

Python for control logic

PostgreSQL for telemetry storage

Threading for parallel execution

🚀 2️⃣ How To Run The Complete System

Follow these steps in order.

✅ Step 1: Start AirSim Simulator

Open the AirSim environment:

Blocks.exe

Wait until the simulation world fully loads.

This initializes:

Drone model

Physics engine

Camera system

Collision system

⚠ Do NOT run Python before AirSim is fully loaded.

✅ Step 2: Activate Virtual Environment

Open PowerShell in your project folder:

cd Desktop\AirSim_Project
venv\Scripts\activate

You should see:

(venv) PS C:\...\AirSim_Project>
✅ Step 3: Install Dependencies (First Time Only)
pip install -r requirements.txt

Installed packages:

airsim

numpy

psycopg2

keyboard

✅ Step 4: Start PostgreSQL

Ensure PostgreSQL server is running.

Make sure database contains:

CREATE TABLE flight_logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    pos_x FLOAT,
    pos_y FLOAT,
    pos_z FLOAT,
    vel_x FLOAT,
    vel_y FLOAT,
    vel_z FLOAT
);
✅ Step 5: Run the Drone System
python main.py
🔄 3️⃣ What Happens Internally When You Run main.py
🔹 Phase 1: System Initialization

main.py performs:

Connect to AirSim

Enable API control

Arm the drone

Takeoff

Move to safe altitude (-8 meters)

Store home position

Start telemetry thread

Start manual control loop

🔹 Phase 2: Telemetry System (Parallel Thread)

telemetry.py runs in background:

Every 0.1 seconds:

Reads drone position

Reads velocity

Prints to console

Inserts data into PostgreSQL

This runs independently of manual control.

Thread safety is ensured using:

threading.Lock()
🔹 Phase 3: Manual Control Loop

User controls drone using keyboard:

Key	Action
W	Forward
S	Backward
A	Rotate Left
D	Rotate Right
Q	Move Up
E	Move Down
R	Return To Home
ESC	Exit

Smooth motion is achieved using interpolation:

current_value += (target_value - current_value) * smoothing_factor

This prevents jerky motion.

🔹 Phase 4: Obstacle Detection

Each control loop:

Depth image captured from AirSim

Converted to numpy array

Minimum distance calculated

If obstacle < 5m → Warning

If obstacle < 2m → Emergency stop

This simulates AI obstacle awareness.

🔹 Phase 5: Collision Handling

If physical collision occurs:

Drone hovers

Emergency landing triggered

System stops

🔹 Phase 6: Return To Home

If user presses R:

Drone moves to stored home position

Hover stabilizes

Control loop exits

🔹 Phase 7: Safe Shutdown

When control exits:

Telemetry thread stops

Database connection closes

Drone disarms

API control disabled

System shuts down cleanly.

🏗 Full Runtime Flow Summary
Start AirSim
    ↓
Activate venv
    ↓
Run main.py
    ↓
Drone Takeoff
    ↓
Telemetry Thread Starts
    ↓
Manual Control Loop
    ↓
Obstacle + Collision Monitoring
    ↓
Return Home OR Exit
    ↓
Telemetry Stops
    ↓
Database Closes
    ↓
Drone Disarmed
📊 What This Demonstrates Technically

This workflow demonstrates:

Real-time robotics control

Multi-threaded system design

Database logging architecture

AI-based perception logic

Modular UAV software design

Safe shutdown engineering

⚠ Important Execution Notes

Always start AirSim before running Python

Do not close AirSim while telemetry is running

Ensure PostgreSQL server is active

Always exit using ESC or R (avoid force closing)

🎯 Final Execution Command Summary
1. Open Blocks.exe
2. Activate venv
3. python main.py
4. Control drone
5. Press ESC to exit








🛠 Installation & Setup Guide
📌 1️⃣ Clone or Download Project

Place the project folder on your Desktop:

Desktop/
   └── AirSim_Project/
🐍 2️⃣ Create Virtual Environment (First Time Only)

Open PowerShell inside the project folder and run:

python -m venv venv

This creates an isolated Python environment inside:

AirSim_Project/venv/
▶ 3️⃣ Activate Virtual Environment

In PowerShell:

venv\Scripts\activate

You should see:

(venv) PS C:\Users\...\AirSim_Project>

This means the virtual environment is active.

📦 4️⃣ Install Required Dependencies
pip install -r requirements.txt

This installs:

airsim

numpy

psycopg2

keyboard

🗄 5️⃣ PostgreSQL Setup

Make sure PostgreSQL is installed and running.

Create the database table:

CREATE TABLE flight_logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    pos_x FLOAT,
    pos_y FLOAT,
    pos_z FLOAT,
    vel_x FLOAT,
    vel_y FLOAT,
    vel_z FLOAT
);

Ensure database credentials in database/db.py are correct.

🚀 Running the Project
Step 1: Start AirSim Simulator

Open:

Blocks.exe

Wait until the environment fully loads.

⚠ Always start AirSim before running Python.

Step 2: Activate Virtual Environment
cd Desktop\AirSim_Project
venv\Scripts\activate
Step 3: Run the Drone System
python main.py
🎮 Drone Controls
Key	Action
W	Move Forward
S	Move Backward
A	Rotate Left
D	Rotate Right
Q	Move Up
E	Move Down
R	Return To Home
ESC	Exit
🔄 Restarting the Project (After Closing)

If you close everything and want to run again:

Open Blocks.exe

Open PowerShell

Activate virtual environment:

venv\Scripts\activate

Run:

python main.py
🧹 Proper Shutdown Procedure

To avoid errors:

Press ESC inside control mode

Wait for:

Telemetry stopped
System shutdown complete

Then close AirSim

⚠ Common Issues & Fixes
Error	Solution
Connection refused	Start AirSim first
Module not found	Activate venv
Database error	Start PostgreSQL
Cursor already closed	Exit properly before closing
📌 Important Notes

Always start AirSim before running Python.

Always activate the virtual environment.

Do not force-close during telemetry logging.

Ensure PostgreSQL service is running.

✅ Quick Command Summary
# Create venv (first time)
python -m venv venv

# Activate
venv\Scripts\activate

# Install packages
pip install -r requirements.txt

# Run project
python main.py
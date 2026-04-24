from drone.controller import DroneController
from drone.teleop import ManualControl
from drone.telemetry import TelemetryLogger
from drone.mission import MissionPlanner
from database.db import Database
from drone.obstacle_ai import ObstacleAvoidanceAI


import threading
import time


def main():
    print("🚀 Starting Drone System...")

    # ---------------- CONTROLLER ----------------
    controller = DroneController()

    controller.client.reset()
    time.sleep(1)

    controller.client.enableApiControl(True)
    controller.client.armDisarm(True)

    controller.takeoff()

    client = controller.get_client()

    # ---------------- THREAD LOCK ----------------
    airsim_lock = threading.Lock()

    # ---------------- MODE SELECTION (FIXED POSITION) ----------------
    mode = input("\nSelect Mode (manual / mission): ").lower()

    # ---------------- DATABASE ----------------
    db = Database()

    # ---------------- TELEMETRY ----------------
    telemetry = TelemetryLogger(client, airsim_lock, db)
    telemetry.start()

    try:

        if mode == "manual":
            print("🎮 Manual Mode Activated")
            manual = ManualControl(client, airsim_lock, controller)
            manual.start()

        elif mode == "mission":
            print("🛰 Mission Mode Activated")

            ai = ObstacleAvoidanceAI(client, airsim_lock)
            
            mission = MissionPlanner(client, airsim_lock,ai)
            mission.execute_mission()

        


        else:
            print(" Invalid mode selected")

    except KeyboardInterrupt:
        print("\n Interrupted by user")

    finally:
        print("\n Shutting down system safely...")

        telemetry.stop()
        db.close()
        controller.shutdown()

        print(" System Shutdown Complete")


if __name__ == "__main__":
    main()
import time


class MissionPlanner:

    def __init__(self, client, lock, ai):
        self.client = client
        self.lock = lock
        self.ai = ai

    def execute_mission(self):

        print("\n🚀 SMART AI MISSION STARTED")

        waypoints = [
            (10, 0, -8),
            (20, 0, -8),
            (20, 10, -8),
            (20, 20, -8),
            (10, 20, -8),
            (0, 20, -8),
            (0, 10, -8),
            (0, 0, -8)
        ]

        for i, wp in enumerate(waypoints):

            print(f"\n📍 Heading to waypoint {i+1}: {wp}")

            reached = False

            while not reached:

                directions = self.ai.analyze_directions()

                if directions is not None:

                    left = directions["left"]
                    center = directions["center"]
                    right = directions["right"]

                    print(f"🧠 L:{left:.2f} C:{center:.2f} R:{right:.2f}")

                    # 🚨 obstacle ahead
                    if center < 5:

                        print("🚧 Obstacle Ahead → Choosing Best Path")

                        # choose safest direction
                        if left > right:
                            print("⬅ Moving LEFT")
                            with self.lock:
                                self.client.moveByVelocityAsync(0, -3, 0, 1).join()

                        else:
                            print("➡ Moving RIGHT")
                            with self.lock:
                                self.client.moveByVelocityAsync(0, 3, 0, 1).join()

                        continue

                # 🚀 Move forward to waypoint
                with self.lock:
                    self.client.moveToPositionAsync(
                        wp[0], wp[1], wp[2], 3
                    ).join()

                reached = True

            time.sleep(1)

        print("✅ SMART MISSION COMPLETED")
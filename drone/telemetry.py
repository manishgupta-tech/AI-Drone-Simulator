import time
import threading


class TelemetryLogger:
    def __init__(self, client, lock, db):
        self.client = client
        self.lock = lock
        self.db = db
        self.running = False
        self.thread = None

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._log_loop)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread is not None:
            self.thread.join()   # Wait for thread to finish safely

    def _log_loop(self):
        print("📡 Live Telemetry + DB Logging Started...")

        while self.running:
            try:
                with self.lock:
                    state = self.client.getMultirotorState()

                pos = state.kinematics_estimated.position
                vel = state.kinematics_estimated.linear_velocity

                print(f"Pos: ({pos.x_val:.2f}, {pos.y_val:.2f}, {pos.z_val:.2f}) "
                      f"| Vel: ({vel.x_val:.2f}, {vel.y_val:.2f}, {vel.z_val:.2f})")

                self.db.insert_telemetry(pos, vel)

                time.sleep(0.2)

            except Exception:
                break

        print("📴 Telemetry Stopped Safely")
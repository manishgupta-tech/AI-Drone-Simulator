import keyboard
import time
import airsim


class ManualControl:
    def __init__(self, client, lock, controller):
        self.client = client
        self.lock = lock
        self.controller = controller

        # -------- SPEED --------
        self.max_speed = 6
        self.current_speed = 0
        self.speed_smoothing = 0.12

        # -------- YAW --------
        self.max_yaw_rate = 90
        self.current_yaw_rate = 0
        self.yaw_smoothing = 0.10

        # -------- VERTICAL --------
        self.vertical_speed = 3
        self.current_vz = 0
        self.vertical_smoothing = 0.15

    def start(self):
        print("\n🎮 PROFESSIONAL SMOOTH MODE")
        print("W/S → Forward/Backward")
        print("A/D → Rotate")
        print("Q/E → Up/Down")
        print("R   → Return To Home")
        print("ESC → Exit\n")

        while True:

            target_speed = 0
            target_yaw = 0
            target_vz = 0

            # -------- INPUT --------
            if keyboard.is_pressed('w'):
                target_speed = self.max_speed
            elif keyboard.is_pressed('s'):
                target_speed = -self.max_speed

            if keyboard.is_pressed('a'):
                target_yaw = -self.max_yaw_rate
            elif keyboard.is_pressed('d'):
                target_yaw = self.max_yaw_rate

            if keyboard.is_pressed('q'):
                target_vz = -self.vertical_speed
            elif keyboard.is_pressed('e'):
                target_vz = self.vertical_speed

            # -------- RETURN TO HOME --------
            if keyboard.is_pressed('r'):
                print("🔁 RETURN TO HOME")
                with self.lock:
                    self.controller.return_to_home()
                break

            if keyboard.is_pressed('esc'):
                print("🛑 Exit Requested")
                break

            # -------- SMOOTH FORWARD --------
            self.current_speed += (target_speed - self.current_speed) * self.speed_smoothing

            # -------- SMOOTH YAW --------
            self.current_yaw_rate += (target_yaw - self.current_yaw_rate) * self.yaw_smoothing

            # -------- SMOOTH VERTICAL --------
            self.current_vz += (target_vz - self.current_vz) * self.vertical_smoothing

            # -------- COLLISION CHECK --------
            with self.lock:
                collision = self.client.simGetCollisionInfo()

            if collision.has_collided and collision.penetration_depth > 0.2:
                print("🚨 HARD COLLISION!")
                with self.lock:
                    self.client.hoverAsync().join()
                    self.client.landAsync().join()
                break

            # -------- APPLY MOVEMENT --------
            with self.lock:
                self.client.moveByVelocityBodyFrameAsync(
                    self.current_speed,
                    0,
                    self.current_vz,
                    0.8,
                    yaw_mode=airsim.YawMode(
                        is_rate=True,
                        yaw_or_rate=self.current_yaw_rate
                    )
                )

            time.sleep(0.15)

        print("🔴 Flight Mode Stopped")
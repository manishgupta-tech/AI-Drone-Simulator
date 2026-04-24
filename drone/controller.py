import airsim


class DroneController:
    def __init__(self):
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)

        self.home_position = None  # IMPORTANT

    def takeoff(self):
        print("🚀 Taking off...")
        self.client.takeoffAsync().join()

        print("⬆ Moving to safe altitude...")
        self.client.moveToZAsync(-8, 3).join()

        self.client.hoverAsync().join()

        # Store home position AFTER reaching altitude
        state = self.client.getMultirotorState()
        self.home_position = state.kinematics_estimated.position

        print("-----> Stable hover achieved.")

    def return_to_home(self):
        if self.home_position is None:
            print("❌ Home position not initialized!")
            return

        print("🏠 RETURN TO HOME ACTIVATED")

        home = self.home_position

        self.client.moveToPositionAsync(
            home.x_val,
            home.y_val,
            home.z_val,
            4
        ).join()

        self.client.hoverAsync().join()
        print("✅ Arrived at Home Position")

    def land(self):
        print("🛬 Landing...")
        self.client.landAsync().join()

    def shutdown(self):
        self.client.armDisarm(False)
        self.client.enableApiControl(False)

    def get_client(self):
        return self.client
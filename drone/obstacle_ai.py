import airsim
import numpy as np


class ObstacleAvoidanceAI:
    def __init__(self, client, lock):
        self.client = client
        self.lock = lock

    def get_depth_image(self):
        try:
            with self.lock:
                responses = self.client.simGetImages([
                    airsim.ImageRequest(
                        0,
                        airsim.ImageType.DepthPerspective,
                        pixels_as_float=True
                    )
                ])

            if not responses:
                return None

            img = responses[0]

            if img.image_data_float is None:
                return None

            depth = np.array(img.image_data_float, dtype=np.float32)
            depth = depth.reshape(img.height, img.width)

            return depth

        except Exception:
            return None

    def analyze_directions(self):
        depth = self.get_depth_image()

        if depth is None:
            return None

        # Split image into 3 parts
        h, w = depth.shape

        left = depth[:, :w//3]
        center = depth[:, w//3:2*w//3]
        right = depth[:, 2*w//3:]

        # Remove invalid values
        left = left[np.isfinite(left)]
        center = center[np.isfinite(center)]
        right = right[np.isfinite(right)]

        if left.size == 0 or center.size == 0 or right.size == 0:
            return None

        return {
            "left": float(np.mean(left)),
            "center": float(np.mean(center)),
            "right": float(np.mean(right))
        }
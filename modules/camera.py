import cv2

class Camera:
    def __init__(self, camera_id=0):
        self.camera = cv2.VideoCapture(camera_id)

    def read(self):
        success, frame = self.camera.read()

        if not success:
            return None

        return frame

    def release(self):
        self.camera.release()
        cv2.destroyAllWindows()
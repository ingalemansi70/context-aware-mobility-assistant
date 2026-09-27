from ultralytics import YOLO
import cv2

class ObjectDetector:
    def __init__(self, model_path="models/yolo11n.pt"):
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model(frame, verbose=False)

        objects = []

        for result in results:
            for box in result.boxes:
                confidence = float(box.conf[0])

                if confidence < 0.5:
                    continue

                class_id = int(box.cls[0])
                name = self.model.names[class_id]

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                objects.append({
                    "name": name,
                    "confidence": confidence,
                    "box": (x1, y1, x2, y2)
                })

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"{name} {confidence:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

        return objects
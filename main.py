
from modules.camera import Camera
from modules.object_detection import ObjectDetector
from modules.face_recognition_module import FaceRecognizer
from modules.voice_assistant import VoiceAssistant

camera = Camera()

object_detector = ObjectDetector(
    "models/yolo11n.pt"
)

face_recognizer = FaceRecognizer(
    "known_faces"
)

voice_assistant = VoiceAssistant()

print()
print("================================")
print(" AI Mobility Assistant Started")
print("================================")
print()
print("Press Q to quit.")

while True:

    frame = camera.read()

    if frame is None:
        print("Camera could not be opened.")
        break

    objects = object_detector.detect(frame)

    faces = face_recognizer.recognize(frame)

    # Objects and faces will be sent to Context Analyzer later

    import cv2

    cv2.imshow(
        "AI Mobility Assistant",
        frame
    )

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

camera.release()

print("Program stopped.")


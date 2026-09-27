import os
import cv2
import face_recognition
import numpy as np

class FaceRecognizer:
    def __init__(self, folder="known_faces"):
        self.folder = folder
        self.known_face_encodings = []
        self.known_face_names = []

        self.load_known_faces()

    def load_known_faces(self):
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
            print("known_faces folder created.")
            return

        for filename in os.listdir(self.folder):
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):

                image_path = os.path.join(self.folder, filename)

                image = face_recognition.load_image_file(image_path)

                encodings = face_recognition.face_encodings(image)

                if len(encodings) > 0:
                    self.known_face_encodings.append(encodings[0])

                    name = os.path.splitext(filename)[0]
                    self.known_face_names.append(name)

                    print("Loaded face:", name)

        if len(self.known_face_names) == 0:
            print("WARNING: No known faces found.")

    def recognize(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(
            rgb_frame,
            model="hog"
        )

        face_encodings = face_recognition.face_encodings(
            rgb_frame,
            face_locations
        )

        faces = []

        for face_encoding, location in zip(
            face_encodings,
            face_locations
        ):

            person = "Unknown"

            if len(self.known_face_encodings) > 0:

                matches = face_recognition.compare_faces(
                    self.known_face_encodings,
                    face_encoding,
                    tolerance=0.50
                )

                distances = face_recognition.face_distance(
                    self.known_face_encodings,
                    face_encoding
                )

                best_index = np.argmin(distances)

                if matches[best_index]:
                    person = self.known_face_names[best_index]

            top, right, bottom, left = location

            faces.append({
                "name": person,
                "box": (left, top, right, bottom)
            })

            cv2.rectangle(
                frame,
                (left, top),
                (right, bottom),
                (255, 0, 0),
                2
            )

            cv2.putText(
                frame,
                person,
                (left, top - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                2
            )

        return faces
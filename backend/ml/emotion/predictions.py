import os
import cv2
import numpy as np
import pathlib

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import tensorflow as tf  # noqa: F401, E402
from keras.models import load_model  # noqa: E402


class EmotionPredictor:
    def __init__(self):
        self.SIZE = 48
        self.OBJECTS = (
            "angry",
            "disgust",
            "fear",
            "happy",
            "sad",
            "surprise",
            "neutral",
        )
        self.model_path = pathlib.Path("ml/emotion/model.h5")
        self.face_path = pathlib.Path("ml/emotion/face.xml")

    def load_model(self):
        if not self.model_path.exists():
            raise FileNotFoundError("Model file not found")
        return load_model(str(self.model_path))

    def load_cascade(self):
        if not self.face_path.exists():
            raise FileNotFoundError("Face cascade file not found")
        return cv2.CascadeClassifier(str(self.face_path))

    def detect_single_face(self, image: bytes) -> np.ndarray:
        face_cascade = self.load_cascade()
        print("Face cascade loaded")
        image = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            image, 1.3, 5, minSize=(self.SIZE, self.SIZE)
        )
        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            face_image = image[y : y + h, x : x + w]
            return face_image
        raise ValueError("No face detected in the image")

    def preprocessing(self, face_image: np.ndarray) -> np.ndarray:
        x = cv2.resize(face_image, (self.SIZE, self.SIZE))
        x = x.reshape(x.shape + (1,))
        x = np.array(x, dtype="float32")
        x = np.expand_dims(x, axis=0)
        if x.max() > 1:
            x = x / 255.0
            return x
        raise ValueError("Invalid image, unable to preprocess")

    def predict(self, image: bytes) -> str:
        model = self.load_model()
        print("Model loaded")
        face_image = self.detect_single_face(image)
        preprocessed = self.preprocessing(face_image)
        predictions = model.predict(preprocessed)
        if isinstance(predictions, np.ndarray):
            return self.OBJECTS[np.argmax(predictions)]
        raise ValueError("Invalid prediction")

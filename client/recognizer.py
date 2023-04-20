# Código baseado em: https://github.com/oarriaga/face_classification

from statistics import mode

import cv2
from keras.models import load_model
import numpy as np

from utils.datasets import get_labels
from utils.inference import detect_faces
from utils.inference import draw_text
from utils.inference import draw_bounding_box
from utils.inference import apply_offsets
from utils.inference import load_detection_model
from utils.preprocessor import preprocess_input


class Recognizer:
    def recognize(self, video_path):
        # Parâmetros para carregamento dos modelos
        model_path = (
            "client/trained_models/detection_models/face_detection/deploy.prototxt"
        )
        weights_path = "client/trained_models/detection_models/face_detection/res10_300x300_ssd_iter_140000.caffemodel"
        net = cv2.dnn.readNetFromCaffe(model_path, weights_path)

        emotion_model_path = "client/trained_models/emotion_model.hdf5"
        emotion_labels = get_labels("fer2013")

        # Carregando os modelos
        emotion_classifier = load_model(emotion_model_path, compile=False)

        # Iniciando a transmissão de vídeo
        cv2.namedWindow("window_frame")
        # video_capture = cv2.VideoCapture(2)
        video_capture = cv2.VideoCapture(video_path)
        while True:
            # Read a frame from the video stream
            ret, frame = video_capture.read()

            # Resize the frame to a fixed size
            resized_frame = None

            try:
                resized_frame = cv2.resize(frame, (300, 300))
            except:
                resized_frame = frame

            # Preprocess the frame (subtract mean and normalize)
            blob = cv2.dnn.blobFromImage(
                resized_frame, 1.0, (300, 300), (104.0, 177.0, 123.0)
            )

            # Pass the preprocessed frame to the face detection model
            net.setInput(blob)
            detections = net.forward()

            # Iterate over the detected faces
            for i in range(detections.shape[2]):
                confidence = detections[0, 0, i, 2]

                # Filter out weak detections
                if confidence > 0.5:
                    # Extract the coordinates of the bounding box
                    box = detections[0, 0, i, 3:7] * np.array(
                        [frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]]
                    )
                    x1, y1, x2, y2 = box.astype("int")

                    # Draw the bounding box around the face
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    # Crop the region of interest (ROI)
                    face_roi = frame[y1:y2, x1:x2]
                    gray_face_roi = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)

                    # Pass the ROI to the emotion recognition model for prediction
                    preprocessed_face_roi = preprocess_input(
                        cv2.resize(gray_face_roi, (64, 64))
                    )
                    emotion_prediction = emotion_classifier.predict(
                        np.expand_dims(preprocessed_face_roi, axis=0)
                    )
                    emotion_label_arg = np.argmax(emotion_prediction)
                    emotion_text = emotion_labels[emotion_label_arg]

                    # Draw the predicted emotion label on the frame
                    cv2.putText(
                        frame,
                        emotion_text,
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,
                        (0, 255, 0),
                        2,
                    )

                    cv2.putText(
                        frame,
                        "Press Q to exit",
                        (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,
                        (0, 255, 0),
                        2,
                    )

            # Display the frame
            cv2.imshow("window_frame", frame)

            # Wait for a key press
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        video_capture.release()
        cv2.destroyAllWindows()

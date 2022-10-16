import time
import tensorflow as tf
from tensorflow.keras.models import model_from_json
import numpy as np


class ExpressionModel(object):
    EMOTIONS_LIST = ["Raiva", "Nojo",
                    "Medo", "Felicidade",
                    "Neutro", "Triste",
                    "Surpresa"]

    def __init__(self, model_json_file, model_weights_file):
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)

        
        self.loaded_model.load_weights(model_weights_file)
        self.loaded_model.make_predict_function()

    def emotionDec(self, img):
        self.preds = self.loaded_model.predict(img)
        return ExpressionModel.EMOTIONS_LIST[np.argmax(self.preds)]

print('[+]Emotion_dec funcionando \n')
time.sleep(2)
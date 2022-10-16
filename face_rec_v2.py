import cv2
import time
import emotion_dec
import numpy as np
import time


faceCasc = cv2.CascadeClassifier('haar_cascade.xml')
model = emotion_dec.ExpressionModel('model.json', 'model_weights.h5')
# font = cv2.FONT_HERSHEY_COMPLEX

file_exp = open('expressions.txt', 'w+')

class Video(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def face_pred(fc, roi):
        prediction = model.emotionDec(roi[np.newaxis, :, :, np.newaxis])
        return prediction
    num_exp = 0

    # Essa função vai pega o face predic, talvez seja substituivel (re estudar)
    def get_video_facedec(self):
        _, fr = self.video.read()
        cor_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        faces = faceCasc.detectMultiScale(cor_fr, 1.3, 5)
      

        for (x, y, w, z) in faces:

            fc = cor_fr[y:y+z, x:x+w]

            roi = cv2.resize(fc, (48, 48))

            # Escreve no console e no arquivo as emoções
            print(Video.face_pred(fc, roi))
            file_exp.write(Video.face_pred(fc, roi) + " \n")

            # Video.num_exp = Video.num_exp + 1

            # cv2.putText(fr, Video.face_pred(fc, roi),
            #             (x, y), font, 0.5, (0, 255, 0), 2)
            # cv2.rectangle(fr, (x, y), (x+w, y+z), (241, 226, 180), 2)

        return fr


def gen(camera):
    # file_exp_read = open("expressions.txt", "r")
    while True:
        # frame = camera.get_video_facedec()
        # real_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Video
        # cv2.imshow('Face_Rec', real_img)

        if cv2.waitKey(1) & 0xFF == ord('q') or Video.num_exp >= 50:

            file_exp.close()
            break

    cv2.destroyAllWindows()
    print('[+]Camera fechada...')

# gen(Video())

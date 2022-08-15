!pip install deepface
!pip install facenet-pytorch

from deepface import DeepFace
import cv2
import torch
import numpy as np
from facenet_pytorch import MTCNN
import requests
from io import BytesIO
from PIL import Image
from PIL import Image, ImageDraw
from PIL import ImageFilter

def face_finder(img_path, confidence=0.90, gender=None, age_min=None, age_max=None, race=None):
    response = requests.get(img_path)
    img = Image.open(BytesIO(response.content))
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)

    mtcnn = MTCNN()
    boxes, confs = mtcnn.detect(img_copy)
    img.show()

    for i in range(len(confs)):
        box = boxes[i]
        conf = confs[i]
        if conf < confidence: continue
        x = box[0]
        y = box[1]
        x2 = box[2]
        y2 = box[3]
        width_half = (x2 - x)/2
        height_half = (y2 - y)/2
        area = (int(x-width_half), int(y-height_half),
                int(x2+width_half), int(y2+height_half) )

        # Crop, show, and save image
        cropped_img = img.crop(area)
        cropped_img.save('cropped_img.jpg')

        try:
          obj = DeepFace.analyze(img_path = 'cropped_img.jpg', actions = ['age', 'gender', 'race'])
        except:
          continue

        if gender == None:
            pass
        elif gender.lower() != obj['gender'].lower():
            continue

        if race == None:
            pass
        elif race.lower() != obj['dominant_race'].lower():
            continue

        if age_min == None:
            pass
        elif age_min > obj['age']:
            continue

        if age_max == None:
            pass
        elif age_max < obj['age']:
            continue

        #print(obj['dominant_race'])
        #print(obj['age'])
        draw.rectangle(box.tolist(), outline=(255, 0, 0), width=1)
    
    return img_copy


address = 'https://s.yimg.com/ny/api/res/1.2/2s9KZ4xwAzhuvWBwMyUuOw--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD02NzU-/https://s.yimg.com/uu/api/res/1.2/qaCUhh7M_aaiDC3pXqH_bQ--~B/aD0yNTU1O3c9NDU0MzthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/pa_viral_news_uk_120/d60fe9052078de58d80102a2ef023d20'

img_copy = face_finder(address, gender='man', race='black' )
img_copy.show()

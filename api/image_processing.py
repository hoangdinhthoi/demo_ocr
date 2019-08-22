import numpy as np
import cv2
import base64
from ocr_demo.settings import IMAGE_HEIGHT


def decode_image(image_base64):
    image = base64.b64decode(image_base64)
    image = np.asarray(bytearray(image), dtype="uint8")
    image = cv2.imdecode(image, cv2.COLOR_BGR2RGB)
    return image

def convert_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def resize(image):
    ratio = image.shape[0] / IMAGE_HEIGHT
    image = cv2.resize(image, (int(image.shape[1]/ratio), IMAGE_HEIGHT))
    return image


def normalize_image(image):
    return image / 255.


def prepare_image(image_base64):
    try:
        image = decode_image(image_base64)
        image = convert_gray(image)
        # cv2.imwrite('/home/hdt/Desktop/1_.jpg', image)
        image = resize(image)
        image = normalize_image(image)
        image = np.expand_dims(image, axis=0)
        image = np.expand_dims(image, axis=-1)
        return image
    except:
        return None



# brtc01020304@

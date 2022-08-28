import tensorflow as tf
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from skimage.transform import resize
from PIL import Image

def preprocess_image(img: Image.Image):
    image = np.asarray(img.resize((224, 224)))[..., :3]
    image = np.expand_dims(image, 0)
    image = image / 127.5 - 1.0
    return image

def load_model():
    waste_model = waste_model = tf.keras.models.load_model('../MobileNetV2/saved_model/waste_model_1.h5')
    waste_model.load_weights('../MobileNetV2/training_1/cp.ckpt')
    return waste_model

def predict_waste_class(img: Image.Image):
    preprocess_img = preprocess_image(img)
    waste_model = load_model()
    predictions = waste_model.predict(preprocess_img)
    max_class_prediction = np.argmax(predictions, axis=1)
    return max_class_prediction[0]

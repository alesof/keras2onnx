import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
import os

verbose = False
dir_name = 'models'
model_name = 'leather_suede.h5'
output_dir_name = 'pb_model'

full_model_path = os.path.join(dir_name, model_name)
output_path = os.path.join(dir_name, output_dir_name)

model = load_model(full_model_path)

if verbose:
    print("\nTensorFlow version:", tf.__version__)
    print("Keras version:", keras.__version__, "\n")
    print("Model path: ", model_path, "\n")

model.summary()
model.save(filepath=output_path, save_format='tf')

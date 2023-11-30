import os
import logging
import argparse
import tensorflow as tf
from tensorflow.keras.models import load_model

def load_and_summary_model(model_path, verbose=False):
    model = load_model(model_path)

    if verbose:
        logging.info("\nTensorFlow version: %s", tf.__version__)
        logging.info("Keras version: %s\n", tf.keras.__version__)
        logging.info("Model path: %s\n", model_path)

    model.summary()
    return model

def save_model_as_tf(model, output_path):
    model.save(filepath=output_path, save_format='tf')

def parse_arguments():
    parser = argparse.ArgumentParser(description="Load TF model.")
    parser.add_argument("model_path", type=str, help="Path to the model file.")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose.")
    return parser.parse_args()

def main():

    args = parse_arguments()

    full_model_path = args.model_path
    output_path = os.path.join(os.path.dirname(full_model_path), 'pb_model')

    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    model = load_and_summary_model(full_model_path, args.verbose)

    save_model_as_tf(model, output_path)

if __name__ == "__main__":
    main()

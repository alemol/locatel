# -*- coding: utf-8 -*-
#
# Created by Alex Molina
# sept 2021
# 
# The code is licensed under the MIT License - see the LICENSE file for details.
# Copyright (c) 2021 Alejandro Molina Villegas

from ml.nlpgeoint import load_cnn_trained, load_subword_encoder
from config import CATEGORIES
import tensorflow as tf
from tensorflow.keras import layers
import tensorflow_datasets as tfds
import numpy as np
import re
import logging
from flask import (Blueprint, request, jsonify)

logging.basicConfig(format='> %(message)s', level=logging.DEBUG)

model = load_cnn_trained()

subpal_encoder = load_subword_encoder()

locatel = Blueprint('locatel', __name__)

@locatel.route('/locatel', methods=['POST'])
def get_class_from_model():

    logging.info('Request received at /locatel -> OK')

    try:
        text = request.json['texto']
    except Exception as e:
        return jsonify({"Aviso": "Verifique los datos de la solicitud. Asegúrese de estar haciendo una solicitud HTTP POST con  header Content-Type: application/json. El cuerpo de la solicitud debe ser un json con un campo llamado \"texto\" codificado en UTF-8. Por ejemplo {\"texto\":\"Solicito alarmas vecinales en mi edificio.\"}"})
        raise e
        logging.info("** CRASH **: unable to read request.json['texto']*")
    logging.info('Text data received  -> OK')

    encoded_input = get_nn_input(text)
    logging.info('Text data encoded  -> OK')

    try:
        predictions = model(encoded_input, training=False).numpy()
    except Exception as e:
        return jsonify({"Aviso": "No fue posible obtener resultados para la solicitud."})
        raise e
        logging.info("** CRASH **: unable to make predictions using model from loaded weights")
    logging.info('Classes predicted  -> OK')
    logging.info("class_vals"+'{}'.format(predictions))

    try:
        response = build_response(text, predictions)
    except Exception as e:
        return jsonify({"Aviso": "No fue posible obtener resultados para la solicitud."})
        raise e
        logging.info("** CRASH **: unable to build the response dict")

    return jsonify(response)


@locatel.route('/', methods=['GET'])
def is_alive():
    return "¡Locatel is Alive!"

def clean_text(text):
    text = re.sub(r'[0-9]+', '', text)
    text = text.lower()
    text = re.sub(r'https?:\/\/.*', '', text)
    text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
    text = re.sub(r'[^\w\s]+', '', text,re.UNICODE)
    text = re.sub(r"\t", ' ', text)
    text = re.sub(r" +", ' ', text)
    text = text.lstrip().rstrip()
    return text

def get_nn_input(text):
    logging.info('* Preprocessing text *')
    prepro_text = clean_text(text)
    logging.info(prepro_text)
    logging.info('* Creating Suword Encoding *')
    #v = np.array(subpal_encoder.encode(prepro_text))
    #encoded_input = tf.keras.preprocessing.sequence.pad_sequences([v], value=0, padding="post", maxlen=PADDING_MAX_LEN)
    encoded_input = np.array([subpal_encoder.encode(text)])
    logging.info(encoded_input)
    return encoded_input

def build_response(text, pred_vals):
    v = pred_vals[0]
    list_labeled = list()
    index_max = np.argmax(v)
    for index, confidence in np.ndenumerate(v):
        logging.info('{}, {}'.format(CATEGORIES[index[0]], confidence))
        list_labeled.append(dict({"motivo":CATEGORIES[index[0]],  "confianza": '{}'.format(confidence)}))
    response_dict= dict({"presunto_motivo":CATEGORIES[index_max],"confianza": '{}'.format(v[index_max]), "texto": text, "valores_confianza": list_labeled})
    return response_dict


# -*- coding: utf-8 -*-
#
# Created by Alex Molina
# sept 2021
# 
# The code is licensed under the MIT License - see the LICENSE file for details.
# Copyright (c) 2021 Alejandro Molina Villegas

import tensorflow as tf
from tensorflow.keras import layers
import tensorflow_datasets as tfds
from config import (SUBWORDS_ENCODER_PATH, ClASSIFICATION_MODEL_PATH, NB_CLASSES)

subword_encoder = tfds.deprecated.text.SubwordTextEncoder.load_from_file(SUBWORDS_ENCODER_PATH)

class DCNN(tf.keras.Model):

    def __init__(self,
                 vocab_size,
                 emb_dim=128,
                 nb_filters=50,
                 FFN_units=512,
                 nb_classes=2,
                 dropout_rate=0.1,
                 training=False,
                 name="dcnn"):
        super(DCNN, self).__init__(name=name)

        self.embedding = layers.Embedding(vocab_size,
                                          emb_dim)
        self.bigram = layers.Conv1D(filters=nb_filters,
                                    kernel_size=2,
                                    padding="valid",
                                    activation="relu")
        self.pool_1 = layers.GlobalMaxPool1D()
        self.trigram = layers.Conv1D(filters=nb_filters,
                                     kernel_size=3,
                                     padding="valid",
                                     activation="relu")
        self.pool_2 = layers.GlobalMaxPool1D()
        self.fourgram = layers.Conv1D(filters=nb_filters,
                                      kernel_size=4,
                                      padding="valid",
                                      activation="relu")
        self.pool_3 = layers.GlobalMaxPool1D()
        self.dense_1 = layers.Dense(units=FFN_units, activation="relu")
        self.dropout = layers.Dropout(rate=dropout_rate)
        if nb_classes == 2:
            self.last_dense = layers.Dense(units=1,
                                           activation="sigmoid")
        else:
            self.last_dense = layers.Dense(units=nb_classes,
                                           activation="softmax")
    
    def call(self, inputs, training):
        x = self.embedding(inputs)
        x_1 = self.bigram(x)
        x_1 = self.pool_1(x_1)
        x_2 = self.trigram(x)
        x_2 = self.pool_2(x_2)
        x_3 = self.fourgram(x)
        x_3 = self.pool_3(x_3)

        merged = tf.concat([x_1, x_2, x_3], axis=-1) # (batch_size, 3 * nb_filters)
        merged = self.dense_1(merged)
        merged = self.dropout(merged, training)
        output = self.last_dense(merged)

        return output


def load_subword_encoder():
    return subword_encoder

def load_cnn_trained():
    new_model = DCNN(vocab_size= subword_encoder.vocab_size, nb_classes=NB_CLASSES, training=False)
    new_model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["sparse_categorical_accuracy"])
    new_model.load_weights(ClASSIFICATION_MODEL_PATH)
    return new_model

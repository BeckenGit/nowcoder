#!/usr/bin/python
#-*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
import os
import data_helpers
from text_cnn import TextCNN

# Parameters
# ==================================================

# Eval Parameters
tf.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
tf.flags.DEFINE_string("checkpoint_dir", "./textclassifier/runs/1470197814/checkpoints/", "Checkpoint directory from training run")

# Misc Parameters
tf.flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
tf.flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")


FLAGS = tf.flags.FLAGS
FLAGS._parse_flags()


def classify(text):
    #Load data. Load your own data here
    sentenses = [text, ]
    # Map data into vocabulary
    vocabulary = data_helpers.get_vocabulary()
    print "vocab:"
    print len(vocabulary)
    x_raw = [data_helpers.clean_str(sentense) for sentense in sentenses]
    print x_raw
    sentenses_digital = []
    for sentense in x_raw:
        sentense_digital = np.zeros(data_helpers.max_len)
        for i, cn_char in enumerate(sentense):
            if cn_char in vocabulary:
                sentense_digital[i] = vocabulary[cn_char]
        sentenses_digital.append(sentense_digital)
    x_test = np.array(sentenses_digital)

    print x_test

    # Evaluation
    # ==================================================
    checkpoint_file = tf.train.latest_checkpoint(FLAGS.checkpoint_dir)
    graph = tf.Graph()
    with graph.as_default():
        session_conf = tf.ConfigProto(
            allow_soft_placement=FLAGS.allow_soft_placement,
            log_device_placement=FLAGS.log_device_placement)
        sess = tf.Session(config=session_conf)
        with sess.as_default():
            # Load the saved meta graph and restore variables
            saver = tf.train.import_meta_graph("{}.meta".format(checkpoint_file))
            saver.restore(sess, checkpoint_file)

            # Get the placeholders from the graph by name
            input_x = graph.get_operation_by_name("input_x").outputs[0]
            # input_y = graph.get_operation_by_name("input_y").outputs[0]
            dropout_keep_prob = graph.get_operation_by_name("dropout_keep_prob").outputs[0]

            # Tensors we want to evaluate
            predictions = graph.get_operation_by_name("output/predictions").outputs[0]

            # Generate batches for one epoch
            batches = data_helpers.batch_iter(list(x_test), FLAGS.batch_size, 1, shuffle=False)

            # Collect the predictions here
            all_predictions = []

            for x_test_batch in batches:
                batch_predictions = sess.run(predictions, {input_x: x_test_batch, dropout_keep_prob: 1.0})
                all_predictions = np.concatenate([all_predictions, batch_predictions])

    labels_list = data_helpers.get_labels_list()
    print all_predictions
    print labels_list
    all_pred_classifies = [labels_list[int(prediction)] for prediction in all_predictions]
    print all_pred_classifies
    return all_pred_classifies[0]

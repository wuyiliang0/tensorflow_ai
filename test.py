# import tensorflow as tf
# g1 = tf.Graph()
# with g1.as_default():
#     v = tf.get_variable("v",shape=[1],initializer=tf.ones_initializer)
# with tf.Session(graph=g1) as sess:
#     tf.global_variables_initializer().run()
#     with tf.variable_scope("",reuse=True):
#         print(sess.run(tf.get_variable("v")));

import cv2
import numpy as np
import os
os.chdir('G:/生日相')
img = cv2.imread('IMG_5000.JPG')

# img = cv2.resize(img,(500,int(img.shape[0]*500/img.shape[1])))
cv2.imshow('hello',img)
cv2.waitKey(0)
